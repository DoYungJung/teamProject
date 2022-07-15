<%@ taglib prefix="fn" uri="http://java.sun.com/jsp/jstl/functions"%>
<%@ taglib prefix="fmt" uri="http://java.sun.com/jsp/jstl/fmt"%>
<%@ taglib prefix="c"      uri="http://java.sun.com/jsp/jstl/core" %>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%> 
    
<!DOCTYPE html>
<html>
	<head>
	<meta charset="UTF-8">
	<title>리뷰 페이지</title>
   
        
	<meta name="viewport" content="width--device-width, initial-scale=1">
	<link rel="stylesheet" href="/css/bootstrap/bootstrap-5.1.3-dist/css/bootstrap.min.css">
	<link rel="stylesheet" href="/css/bootstrap/bootstrap-5.1.3-dist/icon/bootstrap-icons-1.8.3/bootstrap-icons.css">
	<script src="/js/jquery-3.6.0.min.js"></script>
	<script src="/css/bootstrap/bootstrap-5.1.3-dist/js/bootstrap.min.js"></script>
	
	<script type="text/javaScript" language="javascript" defer="defer">
	
	</script>
	

</head>
<body>
<div class="panel-body py-4 my-3"></div>
<c:if test="${!empty sessionScope.userId }">	
	<div class="py-2 text-center container">
		<div class="row py-lg-2">
			<c:if test="${empty restaurantVO.idx}">
    		<h1 class="fw-light">리뷰 등록</h1>
    		<p class="lead text-muted">리뷰 등록 화면입니다.</p>  
    		</c:if>
    		<c:if test="${!empty restaurantVO.idx}">
    		<h1 class="fw-light">리뷰 수정</h1>
    		<p class="lead text-muted">리뷰 수정 화면입니다.</p>  
    		</c:if>
	 	</div> 
	 </div> 
	
	
	
	<div class="container">
		<div class="row">	
    	 <div class="col-sm-2 col-sm-offset-1"></div>
		<div class="col-sm-10 col-sm-offset-1">
    		
			<div class="page-header py-4">
				 <c:if test="${empty restaurantVO.idx}">
					<h4>리뷰  등록</h4>
				 </c:if>
				 <c:if test="${!empty restaurantVO.idx}">
					<h4>리뷰  수정</h4>
				</c:if>
			</div>
    	

   			<c:if test="${! empty sessionScope.userId }">
    		
		
			<div class="panel-body">
			<form class="form-horizontal" id="reviewRegForm" name="reviewRegForm" method="post" action="/">   
	       		
	       		<div class="form-group py-2">
	          		<label class="control-label col-sm-12 for="idx">리뷰아이디:</label>
	          		<div class="col-sm-10">
	          			<input type="text" class="form-control" id="idx" name="idx" placeholder="자동발번" value="${restaurantVO.idx}" >
					</div>
	       		</div>
	       		
	       		<div class="form-group py-2">
	          		<label class="control-label col-sm-2" for="restaurantNo">가게명:</label>
	          		<div class="col-sm-10">
	          			<input type="hidden" class="form-control" id="restaurantNo" name="restaurantNo" placeholder="restaurantVO.restaurantNo 넘겨받아서 꽂고 -> readOnly설정필요" value="${restaurantVO.restaurantNo}" >
	          			<input type="text" class="form-control" id="restaurantNm" name="restaurantNm" placeholder="restaurantVO.restaurantNo 넘겨받아서 꽂고 -> readOnly설정필요" value="${restaurantVO.restaurantNm}" >
					</div>
	       		</div>
	       		
	       		<div class="form-group py-2 col-sm-12">
	       			<label class="control-label col-sm-5" for="regDate">등록자/등록일:</label>
	       			<div class="col-sm-10">
						<input type="text" class="form-control" id="writerNm" name="writerNm" placeholder="placeholder사용자 이름" maxLength="15" style="float:left; width:50%" value="${restaurantVO.writerNm}">
						<input type="hidden" class="form-control" id="writerId" name="writerId" placeholder="사용자 아이디" maxLength="15" style="float:left; width:50%" value="${restaurantVO.writerId}">
						
							<c:set var="regDate" value="${restaurantVO.regDate}"/>
						    <c:if test="fn:length(regDate>8)">
							<c:set var="regDate" value="${fn:substring(regDate,0, fn:length(regDate)-2) }"/>
							</c:if>
						
						<input type="text" class="form-control" id="regDate" name="regDate" placeholder="등록일을 입력하세요" maxLength="15" style="float:left; width:50%" value="${regDate}"> 
					</div>	
				</div>
				
				<p></p><br>
	       		<div class="form-group py-2" >
	       			<label class="control-label col-sm-12" for="content">내용:</label>
		       		<div class="col-sm-10">
		       			<textarea class="form-control" rows="5" id="content" name="content" maxlength="1000">${restaurantVO.content}</textarea>
		       		</div>
	       		</div>
	   		</form>  
	   		</div>
	   		
	   		
	   		
	 
			<div class="footer py-3">
		    	<c:if test="${!empty sessionScope.userId }"> 
		    		<c:if test="${ restaurantVO.idx == null}">
			    	<button type="button" class="btn btn-primary btn-sm" onclick="add();">등록</button>
			    	</c:if>
			    	<c:if test="${  (!empty restaurantVO.idx && !empty sessionScope.userId && (sessionScope.userId == restaurantVO.writerId) )|| (!empty restaurantVO.idx && sessionScope.userId=='admin')}">  
			    	<button type="button" class="btn btn-primary btn-sm" onclick="modify()">수정</button>
			    	</c:if>
		    	</c:if>

		    		
					<button type="button" class="btn btn-primary btn-sm" onclick="history.back()">취소(목록으로)</button>
			</div>
		  
	    	</c:if>
	    </div>
		</div>
		
	</div>
	
	<div id="extraFooterArea" class="py-5"></div>
</c:if>	

<c:if test="${empty sessionScope.userId }">
	<div class="py-2 text-center container">
		<div class="row py-lg-2">
			<c:if test="${empty restaurantVO.idx}">
	   		<h1 class="fw-light">리뷰 페이지</h1>
	   		<p class="lead text-muted">리뷰페이지는 회원전용입니다. <a href="/loginPage.do">로그인</a>  해주세요.</p>
	   		
	   		</c:if>
	 	</div> 
	 </div>
	 <div id="footerExtraArea" class="py-5"></div>
	 <div id="footerExtraArea" class="py-5"></div>
	 <div id="footerExtraArea" class="py-5"></div>
	 <div id="footerExtraArea" class="py-5"></div>
	 <div id="footerExtraArea" class="py-5"></div>
	 <div id="footerExtraArea" class="py-5"></div>
	
</c:if>


</body>



	<script type="text/javaScript" language="javascript" defer="defer">
		$("#btn").click(function(){
			let str = $("#ajaxTestStr").val();
		    let reqUrl = "/ajaxTest.do";
		    $.ajax({
			  type : "POST",
		      url : reqUrl,
		      data : {"ajaxTestStr": str }, 
		      success : function(resp){
		      console.log(resp);
		      $("#resultDiv").append(resp.idx + '<br>');
		      $("#resultDiv").append(resp.title + '<br>');
		      $("#resultDiv").append(resp.content + '<br>');
		      }
		    });
		  });
		
	
		function cancel(){
		
		}
		
		$( document).ready( function(){
			$("#idx").attr("readonly",true);  
			$("#writerNm").attr("readonly",true);
			$("#regDate").attr("readonly",true);
			$("#restaurantNo").attr("readonly",true); 
			$("#restaurantNm").attr("readonly",true); 
		})
		
		var preUrl = document.referrer;
		console.log("이전 url : ", preUrl);
		
		function add(){  
			if($("#title").val()==''){
				alert("제목을 입력하세요");
				$("#title").focus();
				return; 
			}
			if($("#content").val()==''){
				alert("내용을 입력하세요");
				$("#content").focus();
				return;
			}
			if($("#restaurantNo").val()==''){
				alert("가게 아이디가 없으면 등록할 수 없음");
				$("#restaurantNm").focus();
				return;
			}
			if(!confirm("등록하시겠습니까?")){
				return;
			}
			
			document.reviewRegForm.action = "<c:url value='mgmt.do'/>?mode=add"+"&pageLoc=" + preUrl;   
			document.reviewRegForm.submit();
		}
		
		function modify(){
			if($("#title").val()==''){
				alert("제목을 입력하세요");
				$("#title").focus();
				return;
			}
			if($("#content").val()==''){
				alert("내용을 입력하세요");
				$("#content").focus();
				return;
			}
			if(!confirm("수정하시겠습니까?")){
				return;
			}
			
			document.reviewRegForm.action = "<c:url value='mgmt.do'/>?mode=modify&restaurantNo="+${restaurantVO.restaurantNo} +"&pageLoc=" + preUrl;  
			document.reviewRegForm.submit(); 
	
		}
		
		
	</script>

</html>
