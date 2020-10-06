const express = require('express');
const moment = require('moment-timezone');
const router = express.Router();
const email_pattern = /^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$/i;

const db = require(__dirname + '/../db_connect2');

router.get('/edit/:sid', async (req, res)=>{
    const sql = "SELECT * FROM `address_book` WHERE sid=?";
    const [result] = await db.query(sql, [req.params.sid]);
    if(result.length){
        result[0].birthday = moment(result[0].birthday).format('YYYY-MM-DD');
        res.render('/address-book/edit', {row: result[0]});
    } else {
        res.redirect('/address-book/list');
    }
    
});
router.post('/edit', async (req, res)=>{
    const output = {
        success: false,
        body: req.body //表單的資料會放在裡面
    };
    //後端檢查欄位格式
    if(! email_pattern.test(req.body.email)){
        output.error = 'Email 格式不符'
        return res.json(output); //到這邊結束 
    }
    const updateData = { ...req.body }; //代表將req.body展開 類似於複製
    const sid = updateData.sid; 
    delete updateData.sid; //刪除屬性
    const sql = "UPDATE `address_book` SET ? WHERE sid=?";
    const [result] = await db.query(sql, [updateData, sid]);
    if(result.changedRows===1){ //有變更才有
        output.success = true;
    }
    output.result = result;
    res.json(output);
});

router.get('/del/:sid', async (req, res)=>{
    const sql = "DELETE FROM `address_book` WHERE sid=?";
    const [result] = await db.query(sql, [req.params.sid]);
    if(req.get('Referer')){
        res.redirect( req.get('Referer') );
    } else {
        res.redirect('/address-book/list');
    }
});

router.get('/add', (req, res)=>{
    res.locals.pageName = 'address-book-add';
    res.render('/address-book/add');
});
router.post('/add', async (req, res)=>{
    const output = {
        success: false,
        body: req.body //表單的資料會放在裡面
    };
    //後端檢查欄位格式
    if(! email_pattern.test(req.body.email)){
        output.error = 'Email 格式不符'
        return res.json(output); //到這邊結束 
    }

    const sql = "INSERT INTO `address_book` SET ?";
    const [result] = await db.query(sql, [req.body]);
    //if(result.affectedRows){
    if(result.affectedRows===1 && result.insertId){
        output.success = true;
    }
    output.result = result;
    res.json(output);
});

router.get('/list/:page?', async (req, res)=>{
    res.locals.pageName = 'address-book-list';
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