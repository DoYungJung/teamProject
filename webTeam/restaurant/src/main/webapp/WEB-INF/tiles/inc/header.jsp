<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib uri="http://tiles.apache.org/tags-tiles"  prefix="tiles"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>

<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>Insert title here</title>
	<meta name="viewport" content="width--device-width, initial-scale=1">
	<link rel="stylesheet" href="/css/bootstrap/bootstrap-5.1.3-dist/css/bootstrap.min.css">
	<script src="/js/jquery-3.6.0.min.js"></script>
	<script src="/css/bootstrap/bootstrap-5.1.3-dist/js/bootstrap.min.js"></script>
	
	<script type="text/javaScript" language="javascript" defer="defer">
		
	
		function loginFunc() {
			location.href = "<c:url value='/loginPage.do'/>";
		}
		
		function logoutFunc() {
			location.href = "<c:url value='/logout.do'/>";
		}
		
		
		function mgmtReview() {
			location.href = "<c:url value='/reviewList.do'/>";
		}
		
		
		
	</script>
			
	<style>
		
	</style>
</head>
<body>

	<div class="container">
	  <nav class="navbar navbar-expand-lg navbar-white bg-white">
	    <a class="navbar-brand" href="/mainPage.do"><h1><b>KOPO</b></h1></a>Pick Your Restaurant
	  </nav>
	  
	  <div id="optionTab" align="right">
	  
	    <c:if test = "${(empty sessionScope.userId) || (sessionScope.userId == '') }">
	  		<button type="button" class="btn btn-primary" onclick="loginFunc();">로그인</button>
	  	</c:if>
	  	
	  	
	  	
	  	<c:if test = "${!empty sessionScope.userId}">
	  				  ${sessionScope.userNm }님 환영합니다
	  		<button type="button" class="btn btn-primary" onclick="logoutFunc();">로그아웃</button>
	  	</c:if>
	  	
	  	<c:if test = "${sessionScope.userId == 'admin'}">
	  		<button type="button" class="btn btn-primary" onclick="mgmtReview();">리뷰관리</button>
	  	</c:if>
	  	
	  	
	  </div>
	  
	</div>

</body>
</html>