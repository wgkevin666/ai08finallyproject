const express = require('express');
const moment = require('moment-timezone');
const router = express.Router();

const db = require(__dirname + '/../db_connect2');

router.get('/add', (req, res)=>{
    res.render('/address-book/add');
});

router.get('/list/:page?', async (req, res)=>{
    const perPage = 5; //每頁顯示幾筆
    let page = parseInt(req.params.page) || 1; //若無法專換會變成NaN看成false,預設值1
    const output = {
        perPage,
        page,
        totalRows: 0,
        totalPages: 0,
        rows: []
    };

    
    const t_sql = "SELECT COUNT(1) AS num FROM address_book";  //取得總筆數,num昰自己取的
    const [ t_result ] = await db.query(t_sql); 
    output.totalRows = t_result[0].num;  //總筆數, (array第一筆裡面的num)
    output.totalPages = Math.ceil(output.totalRows/perPage) //總頁數, (總筆數/一頁有幾筆,無條件進位)

    //if(output.totalRows===0) 若無資料 直接返回
    if(! output.totalRows){
        return res.render('address-book/list', output);
    }

    if (page<1){
        return res.redirect('/address-book/list/1');
    }
    if (page>output.totalPages){
        return res.redirect('/address-book/list' + output.totalPages);
    }

    const sql = `SELECT * FROM address_book ORDER BY sid DESC LIMIT ${(page-1)*perPage}, ${perPage}`;
    console.log('sql:', sql); //可檢查sql有沒有錯
    const [result] = await db.query(sql);
    result.forEach((el)=>{
        el.birthday = moment(el.birthday).format('YYYY-MM-DD'); //包成moment的物件
    });
    output.rows = result;

    //res.json(result);  看結果
    res.render('address-book/list', output);
});

module.exports = router;