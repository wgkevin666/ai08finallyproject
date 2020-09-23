const express = require('express');
const app = express();
const multer = require ('multer');
//const upload = multer({dest:'tmp_uploads'});
const upload = require(__dirname + '/upload.module');
//const uuid = require('uuid');
const {v4: uuidv4 } = require('uuid');
const { spawn } = require('child_process');

app.set('view engine','ejs');
app.use(express.urlencoded({extended: false}));
app.use(express.json());


const session = require('express-session');
const MySQLstore = require('express-mysql-session')(session);
const db = require(__dirname+'/db_connect2');
const router = express.Router(); 

const sessionStore = new MySQLstore({},db);


// app.get('/test', async (req,res)=>{
//     const sql = "SELECT * FROM `test_book`";
//     const [r]= await db.query(sql)
    
//     res.json(r)
// });

app.get("/",function(request,response){
    //response.render("main",{name:"Weisung"});
    response.render("main");
    //response.send("<h2>Hello Express Success</h2>");
    //response.end("<h2>Hello Express Success</h2>");
});

app.get("/page1",function(request,response){
    response.render("page1");
})
app.post('/try-upload', upload.single('food'), (req, res)=>{
    res.json(req.file);
});
app.post('/try-upload-multi', upload.array('myphoto', 10), (req, res)=>{
    res.json(req.files);
});

app.get("/childpro",function(request,response){
//const ls = spawn('ls', ['-lh', '/usr'])
const ls = spawn('python3', ['/opt/ai08finalproject/function/Food_Recognition/predict.py', '-c', '/opt/ai08finalproject/function/Food_Recognition/config.json', '-i', '/opt/ai08finalproject/function/Food_Recognition/data/test/imgs/img_204.jpg', '-o', '/opt/ai08finalproject/function/Food_Recognition/data/output/']);
ls.stdout.on('data', (data) => {
  console.log(`stdout: ${data}`);
});

ls.stderr.on('data', (data) => {
  console.error(`stderr: ${data}`);
});

ls.on('close', (code) => {
  console.log(`child process exited with code ${code}`);
});    
});

app.get('/try-uuid', (req, res)=>{
    res.json({
        a: uuidv4,
        b: uuidv4,
    });
});


app.post('/try-post', (req, res)=>{
    req.body.加料 = '哈囉';
    res.json(req.body);
});

// app.get("/login",function(request,response){
//     response.render("login");
// });
// app.post("/login", async function(request,response){
//     const output = {
//         success: false,
//         body: request.body
//     };
//     const sql="INSERT INTO `test_book` SET ?"
//     const [r] = await db.query(sql,[request.body])
    

//     if(r.affectedRows===1 && r.insertId) {
//         output.success = true;
//     }
//     response.json(output);
// });

app.get("/try-post-form",function(request,response){
    response.render("try-post-form");
})
app.post("try-post-form" , function(request,response){
    response.render("try-post-form",request.body);
    //response.json(request.body);
})

app.get("/try-qs",function(request,response){
    response.json(request.query);
})

app.get('/test', pythonProcess)

function pythonProcess(req, res) {

  console.log(`name: ${req.query.name}, from: ${req.query.from}`)

  let spawn = require("child_process").spawn

  let process = spawn('python', [
    "./process.py",
    req.query.name,
    req.query.from
  ])

  process.stdout.on('data', (data) => {
    const parsedString = JSON.parse(data)
    res.json(parsedString)
  })

} 



app.use(express.static('public'));

//app.use('/address-book', require(__dirname+'/routes/address-book'));














app.use(express.static('public'));

app.use(function(request,response){
    response.status(404).send("<h2>找不到頁面</h2>");    
});
app.listen(3000,function(){
    console.log("Server Started");
});
