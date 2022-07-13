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
package egovframework.example.sample.restaurant.service;

import java.util.List;

/**
 * @Class Name : EgovSampleService.java
 * @Description : EgovSampleService Class
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
public interface RestaurantService {

	/**
	 * 글을 등록한다.
	 * @param vo - 등록할 정보가 담긴 SampleVO
	 * @return 등록 결과
	 * @exception Exception
	 */
	void insertReview(RestaurantVO restaurantVO) throws Exception;

	/**
	 * 글을 수정한다.
	 * @param vo - 수정할 정보가 담긴 SampleVO
	 * @return void형
	 * @exception Exception
	 */
	void updateReview(RestaurantVO vo) throws Exception;

	/**
	 * 글을 삭제한다.
	 * @param vo - 삭제할 정보가 담긴 SampleVO
	 * @return void형
	 * @exception Exception
	 */
	void deleteReview(RestaurantVO vo) throws Exception;

	/**
	 * 글을 조회한다.
	 * @param vo - 조회할 정보가 담긴 SampleVO
	 * @return 조회한 글
	 * @exception Exception
	 */
	RestaurantVO selectReview(RestaurantVO vo) throws Exception;

	/**
	 * 글 목록을 조회한다.
	 * @param searchVO - 조회할 정보가 담긴 VO
	 * @return 글 목록
	 * @exception Exception
	 */
	List<?> selectReviewList(RestaurantVO searchVO) throws Exception;

	/**
	 * 글 총 갯수를 조회한다.
	 * @param searchVO - 조회할 정보가 담긴 VO
	 * @return 글 총 갯수
	 * @exception
	 */
	int selectReviewListTotCnt(RestaurantVO searchVO);
	
	
	/**
	 * 로그인 아이디의 유저 이름을 조회
	 * @param searchVO - 조회할 정보가 담긴 VO
	 * @return userNm
	 * @exception
	 */
	String selectLoginCheck(RestaurantVO vo);
	
	
	/**
	 * 리뷰 조회수를 +1증가시킨다.
	 * @param searchVO - 조회할 정보가 담긴 VO
	 * @return void형
	 * @exception
	 */
	void updateReviewCount(RestaurantVO vo) throws Exception;
	
	
	//머신러닝 관련 쿼리 메소드
	
	/**
	 * 머신러닝 결과 식당 리스트 조회.
	 * @param searchVO - 조회할 정보가 담긴 VO
	 * @return 글 목록
	 * @exception Exception
	 */
	List<?> selectMachineRunningList(RestaurantVO searchVO) throws Exception;
	
	/**
	 * 전체 식당 리스트 조회.
	 * @param searchVO - 조회할 정보가 담긴 VO
	 * @return 글 목록
	 * @exception Exception
	 */
	List<?> selectTotalList(RestaurantVO searchVO) throws Exception;
	
	/**
	 * 특정 식당 id의 데이터 조회.
	 * @param vo - 특정 식당 index가 담긴 MachineRunningVO
	 * @return 해당 식당의 디테일한 정보 
	 * @exception Exception
	 */
	MachineRunningVO selectRestaurant(RestaurantVO vo) throws Exception;
	
	/**
	 * 식당 총 개수 조회.
	 * @param searchVO 
	 * @return int
	 * @exception
	 */
	int selectRestaurantListTotCnt();
	
	/**
	 * 머신러닝 결과 식당 총 개수 조회.
	 * @param 없음
	 * @return int
	 * @exception
	 */
	int selectMachineRunningListTotCnt(RestaurantVO searchVO);
	
	
	/**
	 * 리뷰등록화면 파라미터 restaurantNo 으로 restaurantNm select하는 함수
	 * @param searchVO - 조회할 정보가 담긴 VO
	 * @return restaurantNm
	 * @exception
	 */
	String selectRestaurantNm(RestaurantVO searchVO);
	

}
