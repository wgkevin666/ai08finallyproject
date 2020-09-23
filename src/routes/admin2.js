const express = require('express');
const router = express.Router();
router.get('/admin2/:action?/:id?', function(request,response){
    response.json(request,params);
});
module.exports = router;