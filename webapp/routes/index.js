var fs = require('fs');
var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

var facedir = '../bing_facecrop/cropped_faces/';


router.get('/images', function (req, res) {
    var files = fs.readdirSync(facedir).filter(function (name) {
        return name.indexOf('_') !== -1 && name.indexOf('.') !== 0;
    }).map(function (name) {
        return name;
    });

    res.send(files);
});

router.post('/labels', function (req, res) {
    var result = req.body['result[]'].join('\n');

    fs.writeFileSync('../ml/results.txt', result);

    res.send("OK")
});

module.exports = router;
