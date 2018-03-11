css = '''
body {
	height: 100vh;
	background-color: #191919;
	font-family: arial;
	color: black;
}

.container {
	display: flex;
	flex-wrap: wrap;
	height: 100%;
	padding: 15%;
	padding-top: 0%;
}

.box {
	position: relative;
	text-align: center;
	width: 100%;
	height: 56%;
	margin-top: 15%;
	border-bottom: solid 5px grey;
	border-top: solid 5px grey;
	background-color: white;
}

img {
	width: 100%;
	height: 100%;
	object-fit: cover;
	transition: opacity .5s;
}

.box:hover img{
	opacity: 0.1;
}

.description {
	position: absolute;
	visibility: hidden;
	opacity: 0;
	transition: opacity .5s, visibility .5s;
}

.box:hover .description {
	visibility: visible;
	opacity: 0.8;
	filter: alpha(opacity=100);
}

.checked {
    color: orange;
}

.main-infos{
	top: 100px;
	left: 25px;
	right: 25px;
}

.more-infos {
	bottom: 100px;
	left: 25px;
	right: 25px;
}

.button {
	color: #E25822;
	cursor: pointer;
}

#overlay {
	position: fixed;
	display: none;
	width: 100%;
	height: 100vh;
	top: 0;
	left: 0;
	right: 0;
	bottom: 0;
	background-color: rgba(0, 0, 0, 0.7);
	z-index: 2;
}

#trailer {
	position: absolute;
	margin-top: 5%;
	margin-left: 10%;
	width: 80%;
	height: 80%;
	z-index: 3;
}

#reviews-container {
	margin: 5%;
	height: 60%;
	background-color: black;
	opacity: 0.8;
	filter: alpha(opacity=80);
	color: white;
	padding: 5%;
	overflow: auto;
}

#title {
	font-size: xx-large;
	color: #E25822;
}

#director, #year, #cast, #genres {
	font-size: small;
	font-style: italic;
}

#storyline {
	font-style: italic;
	padding-top: 1%;
}

@media screen and (min-width: 360px) {
	.box{
		width: 252px;
	}
}

@media screen and (min-width: 380px) {
	.container {
		padding: 0%;
	}
	.box {
		margin: 0 auto;
		margin-top: 15%;
	}
}

@media screen and (min-width: 510px) {
	.container {
		width: 80%;
		margin: 0 auto;
		margin-top: 0%; 
	}
	.box {
		float: left;
		margin-top: 5%;
	}
}
'''

def create_home_page_css():
    home_page_css = open("new_fresh_tomatoes.css", "w")
    home_page_css.write(css)
    home_page_css.close()
