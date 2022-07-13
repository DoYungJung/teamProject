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
		/* pagination 페이지 링크 function */
		function page(pageNo){
				location.href =	"<c:url value='/viewRestaurant.do'/>?restaurantNo="+ ${restaurant.restaurantIdx}+"&pageIndex=" + pageNo;
		}
		
		function modify(idx){
			location.href =	"<c:url value='/mgmt.do'/>?idx=" + idx;
		}

		
		function del(idx, restaurantNo){
	         if(!confirm("삭제하시겠습니까?")){
	            return;
	         }
	         document.form2.action = "<c:url value='mgmt.do'/>?mode=del&idx="+ idx +"&restaurantNo="+restaurantNo;
	         document.form2.submit();

	      }
		
		
		
		
		
	
	</script>



</head>
<body>
	<div class="container">
		<br><br><br><br><br>
		<h1><c:out value="${restaurant.restaurantName }"/></h1>
		
		<div class="store_name_score" data-reactid="60">
			<h3 data-reactid="61" class="text-secondary">
				${restaurant.gubun } <strong data-reactid="63" class="text-warning">${restaurant.score }</strong>
			</h3>
		</div>

		<br>
		
		<div class="my-3 p-3 bg-body rounded shadow-sm">
			<h6 class="border-bottom pb-2 mb-0">
				<p class="text-primary">Restaurant Information</p>
			</h6>
			
			<div class="d-flex text-muted pt-3">
				<svg class="bd-placeholder-img flex-shrink-0 me-2 rounded"
					width="18" height="18" xmlns="http://www.w3.org/2000/svg"
					role="img" aria-label="Placeholder: 18x18"
					preserveAspectRatio="xMidYMid slice" focusable="false">
					<title>업종</title><rect width="100%" height="100%" fill="#007bff"></rect>
					<text x="50%" y="50%" fill="#007bff" dy=".3em">32x32</text></svg>
				<div class="pb-3 mb-0 large lh-sm border-bottom w-100">
					<div class="d-flex justify-content-between">
						<strong class="text-gray-dark">업종</strong>
					</div>
					<span class="d-block">${restaurant.gubun }</span>
				</div>
			</div>
			
			<div class="d-flex text-muted pt-3">
				<svg class="bd-placeholder-img flex-shrink-0 me-2 rounded"
					width="18" height="18" xmlns="http://www.w3.org/2000/svg"
					role="img" aria-label="Placeholder: 18x18"
					preserveAspectRatio="xMidYMid slice" focusable="false">
					<title>주소 정보</title>
					<rect width="100%" height="100%" fill="#007bff"></rect>	
				 	<text x="50%" y="50%" fill="#007bff" dy=".3em">32x32</text></svg>
				<div class="pb-3 mb-0 large lh-sm border-bottom w-100">
					<div class="d-flex justify-content-between">
						<strong class="text-gray-dark">주소</strong>
					</div>
					<span class="d-block"> ${restaurant.address }</span>
				</div>
			</div>
			
			<div class="d-flex text-muted pt-3">
				<svg class="bd-placeholder-img flex-shrink-0 me-2 rounded"
					width="18" height="18" xmlns="http://www.w3.org/2000/svg"
					role="img" aria-label="Placeholder: 18x18"
					preserveAspectRatio="xMidYMid slice" focusable="false">
					<title>전화번호</title><rect width="100%" height="100%" fill="#007bff"></rect>
					<text x="50%" y="50%" fill="#007bff" dy=".3em">32x32</text></svg>
				<div class="pb-3 mb-0 large lh-sm border-bottom w-100">
					<div class="d-flex justify-content-between">
						<strong class="text-gray-dark">전화번호</strong>
					</div>
					<span class="d-block">${restaurant.phone }</span>
				</div>
			</div>
			
			<div class="d-flex text-muted pt-3">
				<svg class="bd-placeholder-img flex-shrink-0 me-2 rounded"
					width="18" height="18" xmlns="http://www.w3.org/2000/svg"
					role="img" aria-label="Placeholder: 18x18"
					preserveAspectRatio="xMidYMid slice" focusable="false">
					<title>영업시간</title><rect width="100%" height="100%" fill="#007bff"></rect>
					<text x="50%" y="50%" fill="#007bff" dy=".3em">32x32</text></svg>
				<div class="pb-3 mb-0 large lh-sm border-bottom w-100">
					<div class="d-flex justify-content-between">
						<strong class="text-gray-dark">영업시간</strong>
					</div>
					<span class="d-block">${restaurant.openingHour }</span>
				</div>
			</div>
			
			<div class="d-flex text-muted pt-3">
				<svg class="bd-placeholder-img flex-shrink-0 me-2 rounded"
					width="18" height="18" xmlns="http://www.w3.org/2000/svg"
					role="img" aria-label="Placeholder: 18x18"
					preserveAspectRatio="xMidYMid slice" focusable="false">
					<title>메뉴</title><rect width="100%" height="100%" fill="#007bff"></rect>
					<text x="50%" y="50%" fill="#007bff" dy=".3em">32x32</text></svg>
				<div class="pb-3 mb-0 large lh-sm border-bottom w-100">
					<div class="d-flex justify-content-between">
						<strong class="text-gray-dark">메뉴</strong>
					</div>
					<span class="d-block"> ${restaurant.menu1 } <br>
						${restaurant.menu2 } <br> ${restaurant.menu3 } <br>
						${restaurant.menu4 }
					</span>
				</div>
			</div>
			
			<div class="d-flex text-muted pt-3">
				<svg class="bd-placeholder-img flex-shrink-0 me-2 rounded"
					width="18" height="18" xmlns="http://www.w3.org/2000/svg"
					role="img" aria-label="Placeholder: 18x18"
					preserveAspectRatio="xMidYMid slice" focusable="false">
					<title>평균가격</title><rect width="100%" height="100%" fill="#007bff"></rect>
					<text x="50%" y="50%" fill="#007bff" dy=".3em">32x32</text></svg>
				<div class="pb-3 mb-0 large lh-sm border-bottom w-100">
					<div class="d-flex justify-content-between">
						<strong class="text-gray-dark">평균가격</strong>
					</div>
					<c:set var="Cprice" value="${restaurant.price}"/>
					<c:if test="${Cprice == '0' ||Cprice == 0}">
					<c:set var="Cprice" value=" "/>
					</c:if>
					<span class="d-block"> ${Cprice} </span>
				</div>
			</div>
		
		
			<div class="d-flex text-muted pt-3">
				<svg class="bd-placeholder-img flex-shrink-0 me-2 rounded"
					width="18" height="18" xmlns="http://www.w3.org/2000/svg"
					role="img" aria-label="Placeholder: 18x18"
					preserveAspectRatio="xMidYMid slice" focusable="false">
					<title>별점</title><rect width="100%" height="100%" fill="#007bff"></rect>
					<text x="50%" y="50%" fill="#007bff" dy=".3em">32x32</text></svg>
				<div class="pb-3 mb-0 large lh-sm border-bottom w-100">
					<div class="d-flex justify-content-between">
						<strong class="text-gray-dark">별점</strong>
					</div>
					<span class="d-block">${restaurant.score } </span>
				</div>
			</div>
			
			<div class="d-flex text-muted pt-3">
				<svg class="bd-placeholder-img flex-shrink-0 me-2 rounded"
					width="18" height="18" xmlns="http://www.w3.org/2000/svg"
					role="img" aria-label="Placeholder: 18x18"
					preserveAspectRatio="xMidYMid slice" focusable="false">
					<title>편의/시설 정보</title><rect width="100%" height="100%"
						fill="#007bff"></rect>
					<text x="50%" y="50%" fill="#007bff" dy=".3em">32x32</text></svg>
				<div class="pb-3 mb-0 large lh-sm border-bottom w-100">
					<div class="d-flex justify-content-between">
						<strong class="text-gray-dark">편의/시설 정보</strong>
					</div>
					<span class="d-block">${restaurant.detailInfo } </span>
				</div>
			</div>
			
			<small class="d-block text-end mt-3">
			
			</small>
		</div>
		
		<!-- 지도를 표시할 div 입니다 -->
		<div id="map" style="width:100%;height:350px;"></div>
		
		<script type="text/javascript" src="//dapi.kakao.com/v2/maps/sdk.js?appkey=8bfea41b5ff14130c5be1d2ecd4217b4"></script>
		
		<script>
		var mapContainer = document.getElementById('map'), // 지도를 표시할 div     
		mapOption = {         
				center: new kakao.maps.LatLng(37.5280443, 127.0389978), // 지도의 중심좌표       
				level: 3 // 지도의 확대 레벨    
		}; 
		// 지도를 표시할 div와  지도 옵션으로  지도를 생성합니다
		var map = new kakao.maps.Map(mapContainer, mapOption);
		
		// 마커가 표시될 위치입니다    
		var markerPosition = new kakao.maps.LatLng(37.5280443, 127.0389978);
		
		// 마커를 생성합니다    
		var marker = new kakao.maps.Marker({        
			position: markerPosition    
		});
		
		
		 // 마커가 지도 위에 표시되도록 설정합니다    
		 marker.setMap(map);
		
		
		
		</script>



	
		<br><br>
		
		<ul class="nav nav-tabs" id="myTab" role="tablist">
		  <li class="nav-item" role="presentation">
		    <button class="nav-link active" id="home-tab" data-bs-toggle="tab" data-bs-target="#home-tab-pane" 
		    type="button" role="tab" aria-controls="home-tab-pane" aria-selected="true">리뷰</button>
		  </li>
		  <li class="nav-item" role="presentation">
		    <a href="/mgmt.do?restaurantNo=${restaurant.restaurantIdx}">
			    <button class="nav-link " id="profile-tab" data-bs-toggle="tab" data-bs-target="#profile-tab-pane" 
			    type="button" role="tab" aria-controls="profile-tab-pane" aria-selected="false" >리뷰작성</button>
		    </a>
		  </li>
		  
		  
		</ul>
		<form method="post" name="form2" action="" method="post" class="border: none">
		<div class="tab-content" id="myTabContent">
		  <div class="tab-pane fade show active" id="home-tab-pane" role="tabpanel" aria-labelledby="home-tab" tabindex="0">
		  	
			  	
		<ul class="list-group list-group-flush">
			  
			  <input type="hidden" name="pageLoc" value="mainPgae"/>
			  	<c:forEach var="result" items="${review}" varStatus="status">
				  	
					  <li class="list-group-item">
					  	<c:out value="${result.writerId}"/> <br><br>
					  	<p class="fs-7">
					  		 
					  		<c:out value="${result.content}"/> 
					  		
					  		<c:if test="${sessionScope.userId == result.writerId || sessionScope.userId == 'admin'}">
						  		<div>
						  		<button type="button" class="btn btn-primary" onclick="modify(${result.idx});">수정</button>
						  		
						  		<button type="button" class="btn btn-danger"  onclick="del(${result.idx}, ${result.restaurantNo})">삭제</button>
						  		</div>
							</c:if>
							
					  	</p>
					  	
						<c:out value="${result.modDate}"/>
						  
					  </li>
				 	
			    </c:forEach>
			    
			    
				    <li class="list-group-item">
				      <!-- /List -->
					  <div id="paging" align="center" class="py-5">
				 			<ui:pagination paginationInfo = "${paginationInfo}" type="image" jsFunction="page" />
				 			<%-- <form:hidden path="pageIndex" /> --%>
				 	  </div>
				    </li>
				    
				</ul>

		  </div>
		</div>
		</form>
	
	</div>



</body>
</html>