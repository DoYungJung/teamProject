package egovframework.example.sample.restaurant.web;

import javax.annotation.Resource;

import org.springframework.stereotype.Controller;
import org.springframework.ui.ModelMap;
import org.springframework.web.bind.annotation.RequestMapping;

import egovframework.example.sample.restaurant.service.RestaurantService;

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

}
