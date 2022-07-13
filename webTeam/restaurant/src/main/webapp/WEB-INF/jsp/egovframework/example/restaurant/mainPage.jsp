<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@ taglib prefix="fmt" uri="http://java.sun.com/jsp/jstl/fmt"%>
<%@ taglib prefix="ui" uri="http://egovframework.gov/ctl/ui"%>

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>main page</title>
<meta name="viewport" content="width--device-width, initial-scale=1">
<link rel="stylesheet"
	href="/css/bootstrap/bootstrap-5.1.3-dist/css/bootstrap.min.css">
<link rel="stylesheet"
	href="/css/bootstrap/bootstrap-5.1.3-dist/icon/bootstrap-icons-1.8.3/bootstrap-icons.css">
<script src="/js/jquery-3.6.0.min.js"></script>
<script src="/css/bootstrap/bootstrap-5.1.3-dist/js/bootstrap.min.js"></script>

<script type="text/javaScript" language="javascript" defer="defer">
		
	 
		
		function runMachineRunning() {
			
			let region = $("#region").val();
			let sex = $("#sex").val();
			let generation = $("#generation").val();
			let options = $("#options").val();
			 
			
			
			if((region == '') || (sex == '') || (generation == '') || (options == '')) {
				alert("조건을 선택해주세요");
			} else {
				document.form1.action = "<c:url value='runMachineRunning.do'/>?region=" + region + "&sex=" + sex + "&generation=" + generation + "&options=" + options;
				document.form1.submit();
				
				
				
				function showLoading() {
					let maskHeight = $(document).height();
					let maskWidth = window.document.body.clientWidth;
					let mask = "<div id='mask' style='position:absolute; z-index:1000; background-color:#000000; left:0; top:0;'></div>";
					
					$('body').append(mask)
					
					$('#mask').css({
						'width':maskWidth
						,'height':maskHeight
						,'opacity':'0.3'
					});
					
					$("#loading").html('<div class="spinner-border text-danger" role="status"><span class="visually-hidden">Loading...</span></div>')
				}
				
				showLoading();
				
				
				
				
			}
			
			
			
		}
		
		function viewRestaurant(restaurantIdx){
    		location.href = "<c:url value='/viewRestaurant.do'/>?restaurantNo=" + restaurantIdx;
   		}
		
		/* pagination 페이지 링크 function */
    	function page(pageNo){
			if( ${select2} == 2 ) {
				location.href =	"<c:url value='/mainPage.do'/>?select2=${select2}&options=${options}&pageIndex="+pageNo;	
			} else {
				location.href =	"<c:url value='/mainPage.do'/>?pageIndex="+pageNo;
			}
   			
    	}
		
		
		
	
	
	
	</script>





<style>
.bd-placeholder-img {
	font-size: 1.125rem;
	text-anchor: middle;
	-webkit-user-select: none;
	-moz-user-select: none;
	user-select: none;
}

@media ( min-width : 768px) {
	.bd-placeholder-img-lg {
		font-size: 3.5rem;
	}
}

.b-example-divider {
	height: 3rem;
	background-color: rgba(0, 0, 0, .1);
	border: solid rgba(0, 0, 0, .15);
	border-width: 1px 0;
	box-shadow: inset 0 .5em 1.5em rgba(0, 0, 0, .1), inset 0 .125em .5em
		rgba(0, 0, 0, .15);
}

.b-example-vr {
	flex-shrink: 0;
	width: 1.5rem;
	height: 100vh;
}

.bi {
	vertical-align: -.125em;
	fill: currentColor;
}

.nav-scroller {
	position: relative;
	z-index: 2;
	height: 2.75rem;
	overflow-y: hidden;
}

.nav-scroller .nav {
	display: flex;
	flex-wrap: nowrap;
	padding-bottom: 1rem;
	margin-top: -1px;
	overflow-x: auto;
	text-align: center;
	white-space: nowrap;
	-webkit-overflow-scrolling: touch;
}

div {
	
}

.aaa {
	width: 1300px;
	height: 400px;
	background: rgba(0, 0, 0, 0.3);
	background-image: url("/images/egovframework/cmmn/background.png");
	margin: auto;
}

.bbb {
	width: 1300px;
	height: 400px;
	padding: 30px;
	text-align: center;
	background-color: #ffffff;
	background-color: rgba(255, 255, 255, 0.6);
}
</style>


</head>
<body>

	<main>

	<div id=loading align="center"></div>

	<section class="py-5 text-center container">
		<div class="aaa">
			<div class="bbb">

				<div class="row py-lg-5">
					<div class="col-lg-6 col-md-8 mx-auto">
					<br>
					<br>
			
						<h1 class="fw-light"><b>당신의 맛집은?</b></h1>

						<p class="lead text-muted"><b>조건을 선택해주세요</b></p>


						<div id="optionArea">
							<form id="form1" name="form1" method="get" action="">
								
								<select id="region" name="region" class="btn btn-warning dropdown-toggle">
							
									<option value=""> 지역 </option>
									<option value="6">신사동</option>

								</select> 
								
								<select id="sex" name="sex" class="btn btn-warning dropdown-toggle">

									<option value=""> 성별 </option>
									<option value="2">남성</option>
									<option value="3">여성</option>


								</select> 
								
								<select id="generation" name="generation" class="btn btn-warning dropdown-toggle">

									<option value=""> 연령 </option>
									<option value="3">청년</option>
									<option value="2">중장년</option>


								</select> 
								
								<select id="options" name="options" class="btn btn-warning dropdown-toggle">

									<option value=""> 옵션 </option>
									<option value="1">가성비</option>
									<option value="2">프리미엄</option>


								</select>

								<button type="button" class="btn btn-secondary"
									id="confirmOptionsBtn" onclick="runMachineRunning();">검색</button>
							</form>


						</div>


					</div>
				</div>
			</div>
		</div>
	</section>

	<div class="album py-5 bg-light">
		<div class="container">

			<div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">

				<c:forEach var="result" items="${resultList}" varStatus="status">
					<div class="col">
						<div class="card shadow-sm">
							<img class="bd-placeholder-img card-img-top" width="100%"
								height="225" xmlns="http://www.w3.org/2000/svg" role="img"
								aria-label="Placeholder: Thumbnail"
								preserveAspectRatio="xMidYMid slice" focusable="false" src="${result.imgPath}">
								<title>Placeholder</title><rect width="100%" height="100%"
									fill="#55595c" />
								<!--  <text x="50%" y="50%" fill="#eceeef" dy=".3em">Image</text>--></img>

							<div class="card-body">
								<p class="card-text">
									<a href="javascript:viewRestaurant('${result.restaurantIdx}');"><c:out
											value="${result.restaurantName}" /></a>
								</p>
								<div class="d-flex justify-content-between align-items-center">
									<small class="text-muted">별점 : <c:out
											value="${result.score}" /></small>
								</div>
							</div>
						</div>
					</div>
				</c:forEach>


			</div>

			<div></div>

			<!-- /List -->
			<div id="paging" align="center" class="py-5">
				<ui:pagination paginationInfo="${paginationInfo}" type="image"
					jsFunction="page" />
				<%-- <form:hidden path="pageIndex" /> --%>
			</div>
		</div>
	</div>


	</main>


</body>
</html>