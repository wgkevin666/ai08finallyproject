const multer = require ('multer');
const {v4: uuidv4 } = require('uuid');

const extMap = {
    'image/jpeg' : '.jpg' ,
    'image/png' : '.png' ,
    'image/gif' : '.gif' ,
    'video/mp4' : '.mp4' ,
    'video/mp3' : '.mp3' ,
}


const storage = multer.diskStorage({
    destination: function (req, file, cb) {
      cb(null, __dirname +'/../public/img-uploads')
    },
    filename: function (req, file, cb) {
        let ext = extMap[file.mimetype];
        if(ext){
            cb(null, uuidv4() + ext) //一定要填空值,如果沒有錯誤的話才會執行
        } else {
            cb(new Error('bad file type'));
        }
            
    }
  })

  const fileFilter = function(req, file, cb){
      cb(null, !!extMap[file.mimetype]); //如果不是那三種圖檔類型會拿到undefine,2個! 轉布林值,是這三個true,不是這三個false
  };

  const upload = multer({storage, fileFilter});

  module.exports = upload;