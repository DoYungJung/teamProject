<%@ taglib prefix="fmt" uri="http://java.sun.com/jsp/jstl/fmt" %>
<%@ taglib prefix="fn" uri="http://java.sun.com/jsp/jstl/functions"%> 
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
   pageEncoding="UTF-8"%>
<%@ taglib prefix="fmt" uri="http://java.sun.com/jsp/jstl/fmt"%>

<%@ taglib prefix="ui" uri="http://egovframework.gov/ctl/ui"%>

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>리뷰 관리 페이지</title>


   <meta name="viewport" content="width--device-width, initial-scale=1">
   <link rel="stylesheet" href="/css/bootstrap/bootstrap-5.1.3-dist/css/bootstrap.min.css">
   <link rel="stylesheet" href="/css/bootstrap/bootstrap-5.1.3-dist/icon/bootstrap-icons-1.8.3/bootstrap-icons.css">
   <script src="/js/jquery-3.6.0.min.js"></script>
   <script src="/css/bootstrap/bootstrap-5.1.3-dist/js/bootstrap.min.js"></script>

   <script type="text/javaScript" language="javascript" defer="defer">
           
 
  
	  
       
   
   $( document).ready( function(){
              <c:if test="${empty sessionScope.userId || sessionScope.userId != 'admin'}">
                 alert("${'관리자에게만 허용된 페이지입니다.'}");
                 location.href = "/mainPage.do";
              </c:if>
           })
   
   </script>


</head>
<body>
	<div class="panel-body py-4 my-3"></div>

	<div class="py-2 text-center container">
		<div class="row py-lg-2">
	     	<h1 class="fw-light">리뷰 관리 화면</h1>
	     	<p class="lead text-muted">리뷰 관리 화면입니다.</p>  
		 </div> 
	</div>
   
 	<div class="panel-body py-5"></div>

 	
   <div class="container">
      <div class="panel panel-default">
     

            <div class="table-responsive py-3">
               <table class="table table-hover table-layout:fixed" >
                  <thead style="text-align: center;" >
                     <tr>
                        <th>No</th>
                        <th>리뷰아이디</th>
                        <th>내용</th>
                        <th>가게명</th>
                        <th>등록자Nm</th>
                        <th>등록자ID</th>
                        <th>등록일</th>
                        <th>수정일</th>
                        <th>Edit</th>
                        <th>Delete</th>
                     </tr>
                  </thead>
                  <tbody>
                     
                     <form class="form-inline" method="post"  name="tableForm" action="">
                     <c:forEach var="result" items="${resultList}" varStatus="status">
                        
                        <tr style="text-align: center"> 
                           <td><c:out value="${paginationInfo.totalRecordCount+1 - ((restaurantVO.pageIndex-1) * restaurantVO.pageSize + status.count)}"/></td>
                           <td><a href="view.do?idx=${result.idx}"><c:out value="${result.idx}" /></a></td>
                           <td style="text-align: left; overflow:hidden; white-space:nowrap; text-overflow:ellipsis; max-width:250px"><a href="javascript:view('${result.idx}');"><c:out value="${result.content}" /></a></td>
                           <td><c:out value="${result.restaurantNm}" /></td>
                           <td><c:out value="${result.writerNm}" /></td>
                           <td><c:out value="${result.writerId}"/></td>
                           <td><fmt:formatDate value="${result.regDate}" pattern="yyyy-MM-dd hh:mm:ss" /></td> 
                           <td><fmt:formatDate value="${result.modDate}" pattern="yyyy-MM-dd hh:mm:ss" /></td> 
                           <td><a href="mgmt.do?idx=${result.idx}"><input type="button"  class="btn btn-primary btn-sm" value="수정"></a></td>
                           <td><button type="button" class="btn btn-danger btn-sm" id="${result.idx}" onclick="del(${result.idx}, ${result.restaurantNo})" >삭제</button></td>
                        
                        </tr>
                     </c:forEach>
         	     </from>
                  </tbody>
               </table>
            </div>
         </div>
         <div class="panel-footer py-2 align=right">
         </div>
      </div>
     
      <div id="paging" style="text-align: center;">
         <ui:pagination paginationInfo="${paginationInfo}" type="image" jsFunction="page" />
         <form:hidden path="pageIndex" />
      </div>
     
      <div id="footerExtraArea" class="py-5"></div>
   </div>


<body>
   <script src="http://code.jquery.com/jquery-latest.min.js"></script>
   <script>
  		
  		let currentUrl = window.location.href;
			console.log("현재 url : ", currentUrl);	
   		let searchFlag = false;
   		let startIndex;
   		let resultUrl;
   		if( currentUrl.includes('search')){
   			searchFlag = true;

   		}
   		
		
       function add(){ 
           location.href = "<c:url value='/mgmt.do'/>";
        }
       
       function view(idx){
           location.href = "<c:url value='/view.do'/>?idx="+idx;
        }
            
      
       

       function page(pageNo){
    	   
          location.href =   "<c:url value='/reviewList.do'/>?pageIndex="+pageNo;
       }
       
   		
       
       
       function page2(pageNo){
    	  
    	   
    	
    	   
    	  
    	   document.searchForm.action = "<c:url value='/reviewList.do'/>?searchCondition=" +$("#searchCondition").val() + "&searchKeyword="+$("#searchKeyword").val()+"&pageIndex="+pageNo + "&pageLoc=" + currentUrl;
    	   document.searchForm.submit();
    	   
       }
       
        function pageTest(pageNo){
           document.listForm.pageIndex.value = pageNo;
           document.listForm.action = "<c:url value='/mainList.do'/>";
              document.listForm.submit();
        }

       function searchCheck(){ 
           if($("#searchKeyword").val() == "" || $("#searchKeyword").val() == null ){
              alert("검색키워드를을 입력하세요");
              return false;
           }
           if($("#searchCondition").val() == "" || $("#searchCondition").val() == null ){
              alert("검색옵션을 선택하세요");
              return false;
           }
           return true; 

        }
   
      function del(idx, restaurantNo){
         if(!confirm("삭제하시겠습니까?")){
            return;
         }
         document.tableForm.action = "<c:url value='mgmt.do'/>?mode=del&idx="+ idx +"&restaurantNo="+restaurantNo;
         document.tableForm.submit();

      }
    
        </script>
</html>
