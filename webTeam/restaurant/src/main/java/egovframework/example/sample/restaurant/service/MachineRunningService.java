package egovframework.example.sample.restaurant.service;


public interface MachineRunningService {
	
	/**
	 * 글을 등록한다.
	 * @param sex - 성별구분
	 * @param generation - 연령구분
	 * @return 등록 결과
	 * @exception Exception
	 */
	void runMachineRunning(int sex, int generation) throws Exception;
}
