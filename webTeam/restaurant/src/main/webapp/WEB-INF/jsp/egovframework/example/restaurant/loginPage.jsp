<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@ taglib prefix="fmt" uri="http://java.sun.com/jsp/jstl/fmt" %>
<%@ taglib prefix="ui" uri="http://egovframework.gov/ctl/ui" %>

<!DOCTYPE html>
<html>
<head>

	<meta charset="UTF-8">
	<title>Insert title here</title>
	<meta name="viewport" content="width--device-width, initial-scale=1">
	<link rel="stylesheet" href="/css/bootstrap/bootstrap-5.1.3-dist/css/bootstrap.min.css">
	<link rel="stylesheet" href="/css/bootstrap/bootstrap-5.1.3-dist/icon/bootstrap-icons-1.8.3/bootstrap-icons.css">
	<script src="/js/jquery-3.6.0.min.js"></script>
	<script src="/css/bootstrap/bootstrap-5.1.3-dist/js/bootstrap.min.js"></script>
	
	<script type="text/javaScript" language="javascript" defer="defer">
	 	 
		/* 비밀번호 입력오류 시 alert창 띄우기*/
		$( document).ready( function(){
	      	<c:if test="${!empty msg}">
	      	alert("${msg}");
	      	</c:if>
	      })
	
	
		/* main 버튼 눌렀을 때 메인페이지로 돌아가기 */
	  	function main() {
	      location.href = "<c:url value='/mainPage.do'/>";
		}
		
		
	   /* 아이디 선택했을 때 비밀번호 자동입력 */
	   function setPwd(user_id) {
	      if (user_id == "admin") {
	         $("#user_pw").val("1234")
	      } else if (user_id == "guest") {
	         $("#user_pw").val("1234")
	      } else {
	         $("#user_pw").val("1234")
	      }
	   }

	   /* 로그인체크 */
	   function check() {
	      if ($("#user_id").val() == "") {
	         alert("아이디를 입력하세요");
	         return false;
	      }
	      if ($("#user_pw").val() == "") {
	         alert("비밀번호를 입력하세요");
	         return false;
	      }
	      return true;
	   }


	
	
	</script>
	
</head>
<body>

	<div class="container">

      <br> <br>

      <c:if
         test="${sessionScope.userId ==null || sessionScope.userId == '' }">
         <form class="form-inline" method="post" action="/login.do">
            <h1 class="h3 mb-3 fw-normal">Please sign in</h1>
            <div class="form-floating">

                <input type="text" class="form-control" id="user_id" name="user_id"
                  placeholder="user_id" onchange="setPwd(this.value);"> <label
                  for="user_id">ID</label>


            </div>

            <div class="form-floating">
               <input type="password" class="form-control" placeholder="Password"
                  id="user_pw" name="user_pw"> <label for="user_pw">Password</label>

            </div>

            <br>
            <button class="w-100 btn btn-lg btn-primary" type="submit"
               onclick="return check();">Sign in</button>
            <br> <br>
            <button type="button" class="w-30 btn btn-md btn-primary"
               onclick="main();" style="float: Right;">main</button>

 
         </form>
      </c:if>


   </div>
	<div id="footerExtraArea" class="py-5"></div>
	<div id="footerExtraArea" class="py-5"></div>
	<div id="footerExtraArea" class="py-5"></div>
</body>
</html>