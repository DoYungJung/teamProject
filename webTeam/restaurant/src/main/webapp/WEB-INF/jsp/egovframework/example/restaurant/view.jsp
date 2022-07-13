<%@ taglib prefix="fn" uri="http://java.sun.com/jsp/jstl/functions"%> 
<%@ taglib prefix="c"      uri="http://java.sun.com/jsp/jstl/core" %>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>

<%@ taglib prefix="fn" uri="http://java.sun.com/jsp/jstl/functions"%>
<% pageContext.setAttribute("crcn", "\r\n");  %>

<%@ taglib prefix="fmt" uri="http://java.sun.com/jsp/jstl/fmt" %>  


<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>KOPO</title>

	<meta name="viewport" content="width--device-width, initial-scale=1">
	<link rel="stylesheet" href="/css/bootstrap/bootstrap-5.1.3-dist/css/bootstrap.min.css">
	<link rel="stylesheet" href="/css/bootstrap/bootstrap-5.1.3-dist/icon/bootstrap-icons-1.8.3/bootstrap-icons.css">
	<script src="/js/jquery-3.6.0.min.js"></script>
	<script src="/css/bootstrap/bootstrap-5.1.3-dist/js/bootstrap.min.js"></script>
        
        <script type="text/javaScript" language="javascript" defer="defer">
   
        	
       	$( document).ready( function(){
   			$("#idx").attr("readonly",true);  
   			$("#writerNm").attr("readonly",true);
   			$("#regDate").attr("readonly",true);
   			$("#restaurantNo").attr("readonly",true); 
   			$("#restaurantNm").attr("readonly",true);
   			$("#content").attr("readonly",true);
   		})
        
        
        function list(){
		location.href = "<c:url value='/reviewList.do'/>";
		}
		
		
		function modify(){
			
			location.href = "<c:url value='/mgmt.do'/>?idx=${restaurantVO.idx}";
		}
		
		function del(){
			
			if(!confirm("삭제하시겠습니까?")){
				return;
			}
			
			document.form1.action = "<c:url value='mgmt.do'/>?mode=del&idx=${restaurantVO.idx}&restaurantNo=${restaurantVO.restaurantNo}"+"&pageLco="+"view&pageIndex="+pageNo;
			document.form1.submit();
			
		}

	
		</script>
        

</head>

<body>
	<div class="panel-body py-4 my-3"></div>
	<div class="py-2 text-center container">
		<div class="row py-lg-2">
	  		<h1 class="fw-light">리뷰 내용</h1>
	  		<p class="lead text-muted">리뷰 상세 내용 화면입니다.</p>  
		</div> 
	</div class="container">

    <div class="container">
    	<div class="row">
	    	<div class="col-sm-2 col-sm-offset-1"></div>
	    	<div class="col-sm-10 col-sm-offset-1">
	    	
	    		<div class="page-header  py-4">
					<h4>리뷰 상세 내용</h4>
				</div>
				
				<div class="panel-body">
					<form class="form-horizontal" method="post" name="form1" action="/"> 
			       		<div class="form-group py-2">
			          		<label class="control-label col-sm-2" for="idx">리뷰아이디:</label>
			          		<div class="col-sm-10" style="text-align:left;">
			          			<input type="text" class="form-control" id="idx" name="idx" value="<c:out value="${restaurantVO.idx}"/>" >
							</div>
			       		</div>
			       		<div class="form-group py-2">
			          		<label class="control-label col-sm-2" for="restaurantNm">가게명:</label>
			          		<div class="col-sm-10 control-label" style="text-align:left;">
			          			<input type="hidden" class="form-control" id="restaurantNo" name="restaurantNo" placeholder="" value="${restaurantVO.restaurantNo}" >
			          			<input type="text" class="form-control" id="restaurantNm" name="restaurantNm" placeholder="" value="<c:out value="${restaurantVO.restaurantNm}"/>" >
							</div>
			       		</div>
			       		
			       		<div class="form-group py-2 col-sm-12">
			       			<label class="control-label col-sm-2" for="pwd">등록자/등록일:</label>
			       			<div class="col-sm-10 control-label" style="text-align:left;">
								
								<input type="text" class="form-control" id="writerNm" name="writerNm" placeholder="placeholder사용자 이름" maxLength="15" style="float:left; width:50%" value="<c:out value="${restaurantVO.writerNm}"/>">
								<c:set var="regDate" value="${fn:substring(restaurantVO.regDate, 0, fn:length(restaurantVO.regDate)-2)}"/> 
								<input type="text" class="form-control" id="regDate" name="regDate" placeholder="등록일을 입력하세요" maxLength="15" style="float:left; width:50%" value="${regDate}"> 
							</div>
						</div>
						
						<p></p><br>
			       		<div class="form-group  py-2">
			       			<label class="control-label col-sm-2" for="pwd">내용:</label>
				       		<div class="col-sm-10 control-label" style="text-align:left;">
				       		
				       		<textarea class="form-control" rows="5" id="content" name="content" maxlength="1000"><c:out value="${fn:replace(restaurantVO.content, crcn, br)}" escapeXml="false"/> </textarea>
				       		</div>
			       		</div>
			   		</form>
			   	</div>
			   	
			   	
			    <div class="py-3 footer"> 
      				<button type="button" class="btn btn-primary btn-sm" onclick="history.back()">목록</button>
			    </div>
		    </div>
	    </div>
	</div>
	<div id="extraFooterArea" class="py-5"></div>
</body>
</html>


