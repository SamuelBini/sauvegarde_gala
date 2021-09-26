var express = require('express');
var router = express.Router();

var connection = require("../bd/connection")


/* GET home page. */
router.get('/', function (req, res, next) {
	res.render('index', { title: 'Express', host: req.hostname });
});

router.get('/parrainage', function (req, res, next) {

	connection.query("SELECT * FROM new_parrainage", function (err, result) {

		console.log(result);
		
		res.render('parrainage', { host: req.hostname, parrainage : result});
		
	})

});


router.post('/record', function (req, res, next) {

	console.log(req.body)

	connection.query(`INSERT INTO presence_winter_night (nom, prenoms, matricule, telephone, email, niveau) VALUES ("${req.body.nom.toUpperCase()}", "${req.body.prenoms.toUpperCase()}", "${req.body.matricule.toUpperCase()}", "${req.body.tel}", "${req.body.email}", "${req.body.niveau}")`, function (err, result) {
		
		if (err) {
			throw err
		}

		else {
			res.redirect("/")
		}

	})

});


module.exports = router;
