const express = require('express');
const { spawn } = require('child_process');
const app = express();
const multer = require('multer');
//const upload = multer({dest:'tmp_uploads'});
const upload = require(__dirname + '/upload.module');
//const uuid = require('uuid');
const { v4: uuidv4 } = require('uuid');

app.set('view engine', 'ejs');
// top-level middlemwares
app.use(express.urlencoded({ extended: false }));
app.use(express.json());

//custom middleware
app.use((req, res, next)=>{
    res.locals.pageName = '';
    next();
});


const session = require('express-session');
const MySQLstore = require('express-mysql-session')(session);
const db = require(__dirname + '/db_connect2');
const router = express.Router();

const sessionStore = new MySQLstore({}, db);

app.use('/admins', require(__dirname + '/routes/admin2'));

// app.get('/test', async (req,res)=>{
//     const sql = "SELECT * FROM `test_book`";
//     const [r]= await db.query(sql)

//     res.json(r)
// });

app.get("/", function (request, response) {
    //res.locals.pageName = 'home';
    //response.render("main",{name:"Weisung"});
    response.render("main");
    //response.send("<h2>Hello Express Success</h2>");
    //response.end("<h2>Hello Express Success</h2>");
});

app.get("/food_recognition", function (request, response) {
    response.render("food_recognition");
})
app.get("/speech", function (request, response) {
    response.render("speech");
})
app.get("/openpose", function (request, response) {
    response.render("openpose");
})

// app.get('/childp', (req, res)=>{
//     const ls = spawn('ls', ['-lh', '/usr']);

//     ls.stdout.on('data', (data) => {
//         console.log(`stdout: ${data}`);
//       });

//       ls.stderr.on('data', (data) => {
//         console.error(`stderr: ${data}`);
//       });

//       ls.on('close', (code) => {
//         console.log(`child process exited with code ${code}`);
//       });

//       res.send('ok');
// });

app.post('/try-upload', upload.single('food'), (req, res) => {


    //res.json(req.file);

    const ls = spawn('python3', ['/opt/ai08finallyproject/function/Food_Recognition/predict.py', '-c', '/opt/ai08finallyproject/function/Food_Recognition/config.json',
        '-i', req.file.path,
        '-o', '/opt/ai08finallyproject/public/img-downloads/']);

    d = ''

    ls.stdout.on('data', (data) => {
        //	result += data
        console.log(`[Nodejs] stdout: ${data}`);
        d = data.toString().split('\n')
        console.log(`[LIST] ${d}`)
        d = d.slice(-2)
        console.log(`[SLICE] ${d}`)
        d = JSON.stringify(d)
        console.log(`[JSON Object] ${d}`)
        //	res.json(`[LIST] ${d}`);
    });

    ls.stderr.on('data', (data) => {
        console.error(`stderr: ${data}`);
    });

    ls.on('close', (code) => {
        //	result = result.split('\n')
        //console.log('[RESULT] ' + result)
        //	   res.json('/opt/ai08finallyproject/public/img-downloads/' + req.file.filename);
        //        console.log(`child process exited with code ${code}`);
        //        res_img = Object.assign({}, req.file)
        //	console.log(req.file)
        //	console.log(typeof(req.file))
        //	res_img['path'].replace('img-uploads', 'img-downloads')
        //	res_img['destination'].replace('img-uploads', 'img-downloads')
        //	console.log(res_img)
        response = {
            filename: req.file.filename,
            data: d
        }
        res.json(response);
    });
});

app.post('/try-upload-wav', upload.single('voice'), (req, res)=>{
    res.json(req.file);
});


app.post('/try-upload-multi', upload.array('myphoto', 10), (req, res) => {
    res.json(req.files);
});


app.get('/try-uuid', (req, res) => {
    res.json({
        a: uuidv4,
        b: uuidv4,
    });
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

app.get("/try-post-form", function (request, response) {
    response.render("try-post-form");
})
app.post("try-post-form", function (request, response) {
    response.render("try-post-form", request.body);
    //response.json(request.body);
})

app.get("/try-qs", function (request, response) {
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



//app.use('/address-book', require(__dirname + '/routes/address-book'));
app.use(express.static('public'));







app.use(express.static('public'));

app.use(function (request, response) {
    response.status(404).send("<h2>找不到頁面</h2>");
});
app.listen(3000, function () {
    console.log("Server Started");
});
