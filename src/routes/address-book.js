const express = require('express');
const router = express.Router();

const db = require(__dirname + '/../db_connect2');

router.get('/list/:page?', async (req, res)=>{
    let page = parseInt(req.params.page) || 1; //若無法專換會變成NaN看成false,預設值1
    const perPage = 5; //每頁顯示幾筆
    const sql = `SELECT * FROM address_book LIMIT ${(page-1)*perPage}, ${perPage}`;
    console.log('sql:', sql); //可檢查sql有沒有錯
    const [result] = await db.query(sql);

    //res.json(result);  看結果
    res.render('address-book/list', {rows: result});
});

module.exports = router;