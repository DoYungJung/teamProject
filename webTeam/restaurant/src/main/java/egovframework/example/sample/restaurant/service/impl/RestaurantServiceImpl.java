/*
 * Copyright 2008-2009 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package egovframework.example.sample.restaurant.service.impl;

import java.util.List;

import javax.annotation.Resource;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Service;

import egovframework.example.sample.restaurant.service.MachineRunningVO;
import egovframework.example.sample.restaurant.service.RestaurantService;
import egovframework.example.sample.restaurant.service.RestaurantVO;
import egovframework.rte.fdl.cmmn.EgovAbstractServiceImpl;
import egovframework.rte.fdl.idgnr.EgovIdGnrService;

/**
 * @Class Name : EgovSampleServiceImpl.java
 * @Description : Sample Business Implement Class
 * @Modification Information
 * @
 * @  수정일      수정자              수정내용
 * @ ---------   ---------   -------------------------------
 * @ 2009.03.16           최초생성
 *
 * @author 개발프레임웍크 실행환경 개발팀
 * @since 2009. 03.16
 * @version 1.0
 * @see
 *
 *  Copyright (C) by MOPAS All right reserved.
 */

@Service("restaurantService")
public class RestaurantServiceImpl extends EgovAbstractServiceImpl implements RestaurantService {

	private static final Logger LOGGER = LoggerFactory.getLogger(RestaurantServiceImpl.class);

	/** SampleDAO */
	// TODO ibatis 사용
	//@Resource(name = "sampleDAO")
	//private SampleDAO sampleDAO;
	// TODO mybatis 사용
    @Resource(name="restaurantMapper")
	private RestaurantMapper restaurantDAO;

	/** ID Generation */
	@Resource(name = "egovIdGnrService")
	private EgovIdGnrService egovIdGnrService;

	/**
	 * 글을 등록한다.
	 * @param vo - 등록할 정보가 담긴 SampleVO
	 * @return 등록 결과
	 * @exception Exception
	 */
	@Override
	public void insertReview(RestaurantVO restaurantVO) throws Exception {
		LOGGER.debug(restaurantVO.toString());

		restaurantDAO.insertReview(restaurantVO);
	}

	/**
	 * 글을 수정한다.
	 * @param vo - 수정할 정보가 담긴 SampleVO
	 * @return void형
	 * @exception Exception
	 */
	@Override
	public void updateReview(RestaurantVO vo) throws Exception {
		restaurantDAO.updateReview(vo);
	}

	/**
	 * 글을 삭제한다.
	 * @param vo - 삭제할 정보가 담긴 SampleVO
	 * @return void형
	 * @exception Exception
	 */
	@Override
	public void deleteReview(RestaurantVO vo) throws Exception {
		restaurantDAO.deleteReview(vo);
	}

	/**
	 * 글을 조회한다.
	 * @param vo - 조회할 정보가 담긴 SampleVO
	 * @return 조회한 글
	 * @exception Exception
	 */
	@Override
	public RestaurantVO selectReview(RestaurantVO vo) throws Exception {
		RestaurantVO resultVO = restaurantDAO.selectReview(vo);
		if (resultVO == null) {
			resultVO = new RestaurantVO();
			//throw processException("info.nodata.msg");
		}
		return resultVO;
	}

	/**
	 * 글 목록을 조회한다.
	 * @param searchVO - 조회할 정보가 담긴 VO
	 * @return 글 목록
	 * @exception Exception
	 */
	@Override
	public List<?> selectReviewList(RestaurantVO searchVO) throws Exception {
		return restaurantDAO.selectReviewList(searchVO);
	}

	/**
	 * 글 총 갯수를 조회한다.
	 * @param searchVO - 조회할 정보가 담긴 VO
	 * @return 글 총 갯수
	 * @exception
	 */
	@Override
	public int selectReviewListTotCnt(RestaurantVO searchVO) {
		return restaurantDAO.selectReviewListTotCnt(searchVO);
	}
	
	
	
	/**
	 * 로그인 아이디의 유저 이름을 조회
	 * @param searchVO - 조회할 정보가 담긴 VO
	 * @return userNm
	 * @exception
	 */
	@Override
	public String selectLoginCheck(RestaurantVO searchVO) {
		return restaurantDAO.selectLoginCheck(searchVO);
	}

	/**
	 * 리뷰 조회수를 +1증가시킨다.
	 * @param searchVO - 조회할 정보가 담긴 VO
	 * @return void형
	 * @exception
	 */
	@Override
	public void updateReviewCount(RestaurantVO vo) throws Exception {
		restaurantDAO.updateReviewCount(vo);
	}
	
	/**
	 * 머신러닝 결과 테이블을 조회.
	 * @param searchVO - 조회할 정보가 담긴 VO
	 * @return 글 목록
	 * @exception Exception
	 */
	@Override
	public List<?> selectMachineRunningList(RestaurantVO searchVO) throws Exception {
		return restaurantDAO.selectMachineRunningList(searchVO);
	}
	
	/**
	 * 식당 전체 테이블을 조회.
	 * @param searchVO - 조회할 정보가 담긴 VO
	 * @return 글 목록
	 * @exception Exception
	 */
	@Override
	public List<?> selectTotalList(RestaurantVO searchVO) throws Exception {
		return restaurantDAO.selectTotalList(searchVO);
	}
	
	/**
	 * 글을 조회한다.
	 * @param vo - 조회할 정보가 담긴 SampleVO
	 * @return 조회한 글
	 * @exception Exception
	 */
	@Override
	public MachineRunningVO selectRestaurant(RestaurantVO vo) throws Exception {
		MachineRunningVO resultVO = restaurantDAO.selectRestaurant(vo);
//		if (resultVO == null)
//			throw processException("info.nodata.msg");
		return resultVO;
	}
	
	
	/**
	 * 식당 총 개수 조회.
	 * @param 없음
	 * @return int
	 * @exception
	 */
	@Override
	public int selectRestaurantListTotCnt() {
		return restaurantDAO.selectRestaurantListTotCnt();
	}
	
	/**
	 * 머신러닝 결과 식당 총 개수 조회.
	 * @param 없음
	 * @return int
	 * @exception
	 */
	@Override
	public int selectMachineRunningListTotCnt(RestaurantVO searchVO) {
		return restaurantDAO.selectMachineRunningListTotCnt(searchVO);
	}
	
	
	@Override
	public String selectRestaurantNm(RestaurantVO searchVO) {
		return restaurantDAO.selectRestaurantNm(searchVO);
	}
	


}
