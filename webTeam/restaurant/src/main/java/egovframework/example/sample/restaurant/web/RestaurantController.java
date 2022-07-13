package egovframework.example.sample.restaurant.web;

import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.List;

import javax.annotation.Resource;
import javax.servlet.http.HttpServletRequest;

import org.springframework.stereotype.Controller;
import org.springframework.ui.ModelMap;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;

import egovframework.example.sample.restaurant.service.MachineRunningService;
import egovframework.example.sample.restaurant.service.MachineRunningVO;
import egovframework.example.sample.restaurant.service.RestaurantService;
import egovframework.example.sample.restaurant.service.RestaurantVO;
import egovframework.rte.fdl.property.EgovPropertyService;
import egovframework.rte.ptl.mvc.tags.ui.pagination.PaginationInfo;

@Controller
public class RestaurantController {
	
	@Resource(name = "propertiesService")
	protected EgovPropertyService propertiesService;

	
	@Resource(name="restaurantService")
	private RestaurantService restaurantService;
	
	@Resource(name="machineRunningService")
	private MachineRunningService machineRunningService;


	
	@RequestMapping(value = "/mainPage.do")
	public String mainPage(@ModelAttribute("restaurantVO") RestaurantVO restaurantVO, ModelMap model) throws Exception {
		
		int totCnt = 0;
		
		//페이징처리
		restaurantVO.setPageUnit(propertiesService.getInt("pageUnit"));
		restaurantVO.setPageSize(propertiesService.getInt("pageSize"));
		/** pageing setting */
		PaginationInfo paginationInfo = new PaginationInfo(); 
		paginationInfo.setCurrentPageNo(restaurantVO.getPageIndex());  
		paginationInfo.setRecordCountPerPage(restaurantVO.getPageUnit());  
		paginationInfo.setPageSize(restaurantVO.getPageSize()); 
		restaurantVO.setFirstIndex(paginationInfo.getFirstRecordIndex());
		restaurantVO.setLastIndex(paginationInfo.getLastRecordIndex());
		restaurantVO.setRecordCountPerPage(paginationInfo.getRecordCountPerPage());
		
		if(restaurantVO.getSelect2() == 2) {
			//select2가 2이면 머신러닝 결과 조회
			System.out.println("options test : " + restaurantVO.getOptions());
			List<?> list = restaurantService.selectMachineRunningList(restaurantVO);
			
			
			
			model.addAttribute("resultList", list);
			model.addAttribute("select2", restaurantVO.getSelect2());
			model.addAttribute("options", restaurantVO.getOptions());
			
			totCnt = restaurantService.selectMachineRunningListTotCnt(restaurantVO);
		} else {
			//그 이외이면 기본 결과가 조회
			List<?> list = restaurantService.selectTotalList(restaurantVO);
			
			 
			model.addAttribute("resultList", list);
			model.addAttribute("select2", restaurantVO.getSelect2());
			
			totCnt = restaurantService.selectRestaurantListTotCnt();
		}
		
		
		paginationInfo.setTotalRecordCount(totCnt);  
		model.addAttribute("paginationInfo", paginationInfo);
		
		return "/restaurant/mainPage";
	}
	
	
	// jcraft 실행 end-point
	@RequestMapping(value = "/runMachineRunning.do", method =RequestMethod.GET)
	public String runMachineRunneing(ModelMap model, @RequestParam("sex") int sex,
		@RequestParam("generation") int generation, @RequestParam("options") int options) throws Exception {
		
		System.out.println("sex : " + sex);
		System.out.println("generation : " + generation);
		System.out.println("options : " + options);
		
		machineRunningService.runMachineRunning(sex, generation);
		
		return "redirect:/mainPage.do?select2=2&options=" + options;
		
		
	}
	
	// 상세 식당페이지 end-point
	// 리뷰정보 모두 출력 (단, 해당 식당 id로만)
	@RequestMapping(value = "/viewRestaurant.do", method =RequestMethod.GET)
	public String viewRestaurant(ModelMap model, @ModelAttribute("restaurantVO") RestaurantVO restaurantVO) throws Exception {
		
		System.out.println("식당 id : " + restaurantVO.getRestaurantNo());
		MachineRunningVO machineRunningVO = restaurantService.selectRestaurant(restaurantVO);
		
		//페이징처리
		restaurantVO.setPageUnit(propertiesService.getInt("pageUnit"));
		restaurantVO.setPageSize(propertiesService.getInt("pageSize"));
		/** pageing setting */
		PaginationInfo paginationInfo = new PaginationInfo(); 
		paginationInfo.setCurrentPageNo(restaurantVO.getPageIndex());  
		paginationInfo.setRecordCountPerPage(restaurantVO.getPageUnit());  
		paginationInfo.setPageSize(restaurantVO.getPageSize()); 
		restaurantVO.setFirstIndex(paginationInfo.getFirstRecordIndex());
		restaurantVO.setLastIndex(paginationInfo.getLastRecordIndex());
		restaurantVO.setRecordCountPerPage(paginationInfo.getRecordCountPerPage());
		
		List<?> list = restaurantService.selectReviewList(restaurantVO);
		
		
		model.addAttribute("restaurant", machineRunningVO);
		model.addAttribute("review", list);
		
		
		int totCnt = restaurantService.selectReviewListTotCnt(restaurantVO);
		paginationInfo.setTotalRecordCount(totCnt);  
		model.addAttribute("paginationInfo", paginationInfo);
		
		return "/restaurant/viewRestaurant";
		
	}
	
	// 로그인페이지 이동
    @RequestMapping(value = "/loginPage.do")
    public String loginPage(ModelMap model) throws Exception {
    	return "/restaurant/loginPage";
    }
    
    
	// 로그인 실행
    @RequestMapping(value = "/login.do")
    public String login(@RequestParam("user_id") String user_id, @RequestParam("user_pw") String user_pw,
          ModelMap model, HttpServletRequest request) throws Exception {
       System.out.println("userid:" + user_id);
       System.out.println("password:" + user_pw);

       RestaurantVO restaurantVO = new RestaurantVO();
       restaurantVO.setUserId(user_id);
       restaurantVO.setUserPw(user_pw);
       String user_name = restaurantService.selectLoginCheck(restaurantVO);

       if (user_name != null && !"".equals(user_name)) {
          request.getSession().setAttribute("userId", user_id);
          request.getSession().setAttribute("userNm", user_name);
          return "redirect:/mainPage.do";
          
       } else {
          request.getSession().setAttribute("userId", "");
          request.getSession().setAttribute("userNm", "");
          model.addAttribute("msg", "사용자 정보가 올바르지 않습니다.");
          return "/restaurant/loginPage";
       }

       
       
    }
	    
	    
    // 로그아웃
    @RequestMapping(value = "/logout.do")
    public String logout(ModelMap model, HttpServletRequest request) throws Exception {
       request.getSession().invalidate();
       return "redirect:mainPage.do";
    }


  
    //댓글 등록 화면 & 수정 화면
  	@RequestMapping(value = "/mgmt.do", method=RequestMethod.GET)
  	public String review1(ModelMap model, @ModelAttribute("restaurantVO") RestaurantVO restaurantVO, HttpServletRequest request) throws Exception {
  		
  		
  		SimpleDateFormat sdf = new SimpleDateFormat("yyyyMMdd");
  		Calendar c1 = Calendar.getInstance();
  		String strToday = sdf.format(c1.getTime());
  			
  		restaurantVO.setRegDate(strToday);
  		try {
  			restaurantVO.setWriterId(request.getSession().getAttribute("userId").toString());
  	  		restaurantVO.setWriterNm(request.getSession().getAttribute("userNm").toString());
  	  		
  	  		if(restaurantVO.getIdx() != null) {
  	  			restaurantVO = restaurantService.selectReview(restaurantVO);
  	  			model.addAttribute("restaurantVO", restaurantVO);
  	  			
  	  		}
  	  		else {
  	  			String restaurantNm = restaurantService.selectRestaurantNm(restaurantVO);
  	  	  		restaurantVO.setRestaurantNm(restaurantNm);
  	  	  		model.addAttribute("restaurantVO", restaurantVO);
  	  	  		
  	  		}
		} catch (Exception e) {
			System.out.println(e);
		}
  		
  		return "/restaurant/mgmt";
  	}
  	
  	
    //댓글 수정,등록,삭제 버튼 눌렀을시 받는 라우터
  	@RequestMapping(value = "/mgmt.do", method=RequestMethod.POST)
  	public String review2(ModelMap model, @RequestParam("mode") String mode, @ModelAttribute("restaurantVO") RestaurantVO restaurantVO,
  			HttpServletRequest request) throws Exception {
  		if("add".equals(mode)) {
  			restaurantService.insertReview(restaurantVO);
  			
  			
  			String preUrl = restaurantVO.getPageLoc(); 
  			return  "redirect:"+preUrl;
  			
  		} else if("modify".equals(mode)) {
  			restaurantService.updateReview(restaurantVO);
  			
  			
  			String preUrl = restaurantVO.getPageLoc();
			return  "redirect:"+preUrl;
  			 
  		} else if("del".equals(mode)) {
  			restaurantService.deleteReview(restaurantVO);
  			String referer = request.getHeader("Referer"); 
			return "redirect:"+ referer;
  		}
  		return "redirect:/reviewList.do"; 
  	}
  	
  	
	//리뷰 내용 상세 페이지
	@RequestMapping(value = "/view.do", method=RequestMethod.GET)
	public String view(HttpServletRequest request, ModelMap model) throws Exception {
		RestaurantVO restaurantVO = new RestaurantVO();
		String idx = request.getParameter("idx");
		restaurantVO.setIdx(idx);
		
		restaurantService.updateReviewCount(restaurantVO);

		restaurantVO = restaurantService.selectReview(restaurantVO);
	    model.addAttribute("restaurantVO", restaurantVO);

	    return "/restaurant/view"; 
	}
	
	
	@RequestMapping(value = "/reviewList.do")
	public String list(@ModelAttribute("restaurantVO") RestaurantVO restaurantVO, ModelMap model) throws Exception {
		restaurantVO.setPageUnit(propertiesService.getInt("pageUnit"));
		restaurantVO.setPageSize(propertiesService.getInt("pageSize"));
		/** pageing setting */
		PaginationInfo paginationInfo = new PaginationInfo(); 
		paginationInfo.setCurrentPageNo(restaurantVO.getPageIndex());  
		paginationInfo.setRecordCountPerPage(restaurantVO.getPageUnit());  
		paginationInfo.setPageSize(restaurantVO.getPageSize()); 
		restaurantVO.setFirstIndex(paginationInfo.getFirstRecordIndex());
		restaurantVO.setLastIndex(paginationInfo.getLastRecordIndex());
		restaurantVO.setRecordCountPerPage(paginationInfo.getRecordCountPerPage());

		List<?> list = restaurantService.selectReviewList(restaurantVO);
		model.addAttribute("resultList", list);

		int totCnt = restaurantService.selectReviewListTotCnt(restaurantVO);
		
		paginationInfo.setTotalRecordCount(totCnt);
		model.addAttribute("paginationInfo", paginationInfo);

		return "/restaurant/reviewList";
	}
	
	
	@RequestMapping(value = "/reviewList.do", method=RequestMethod.POST)
	public String list2(@ModelAttribute("restaurantVO") RestaurantVO restaurantVO, ModelMap model) throws Exception {
		restaurantVO.setPageUnit(propertiesService.getInt("pageUnit"));
		restaurantVO.setPageSize(propertiesService.getInt("pageSize"));
		/** pageing setting */
		PaginationInfo paginationInfo = new PaginationInfo(); 
		paginationInfo.setCurrentPageNo(restaurantVO.getPageIndex());  
		paginationInfo.setRecordCountPerPage(restaurantVO.getPageUnit());  
		paginationInfo.setPageSize(restaurantVO.getPageSize()); 
		restaurantVO.setFirstIndex(paginationInfo.getFirstRecordIndex());
		restaurantVO.setLastIndex(paginationInfo.getLastRecordIndex());
		restaurantVO.setRecordCountPerPage(paginationInfo.getRecordCountPerPage());

		List<?> list = restaurantService.selectReviewList(restaurantVO);
		model.addAttribute("resultList", list);
		
		int totCnt = restaurantService.selectReviewListTotCnt(restaurantVO);
		
		paginationInfo.setTotalRecordCount(totCnt);
		model.addAttribute("paginationInfo", paginationInfo);

		return "/restaurant/reviewList";
		
	}
	
	

}
