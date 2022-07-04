package egovframework.example.sample.restaurant.web;

import java.text.SimpleDateFormat;
import java.util.Calendar;

import javax.annotation.Resource;
import javax.servlet.http.HttpServletRequest;

import org.springframework.stereotype.Controller;
import org.springframework.ui.ModelMap;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.RequestMapping;

import egovframework.example.sample.restaurant.service.RestaurantService;
import egovframework.example.sample.restaurant.service.RestaurantVO;

@Controller
public class RestaurantController {
	
	@Resource(name="restaurantService")
	private RestaurantService restaurantService;

	
	@RequestMapping(value = "/mainPage.do")
	public String mainPage(ModelMap model) throws Exception {
		return "/restaurant/mainPage";
	}
	
	// 모든 페이지에 레이아웃 적용 테스트 end-poin
	@RequestMapping(value = "/testLayout.do")
	public String test1(ModelMap model) throws Exception {
		return "/restaurant/testLayout";
	}
	
	@RequestMapping(value = "/mgmt.do")
	public String reviewList(ModelMap model,  @ModelAttribute("restaurantVO") RestaurantVO restaurantVO, HttpServletRequest request) throws Exception {
		
		SimpleDateFormat sdf = new SimpleDateFormat("yyyyMMdd");
		Calendar c1 = Calendar.getInstance();
		String strToday = sdf.format(c1.getTime());
		
//		restaurantVO.setRegDate(regDate);(strToday);
//		restaurantVO.setWriterId(writerId);(request.getSession().getAttribute("userId").toString()); //댓글등록할 유저네임 자동뿌려줘야해서
//		restaurantVO.setWriterNm(request.getSession().getAttribute("userName").toString());
		return "/restaurant/mgmt";
	}

}
