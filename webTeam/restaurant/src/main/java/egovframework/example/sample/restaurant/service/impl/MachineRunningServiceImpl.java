package egovframework.example.sample.restaurant.service.impl;

import java.io.InputStream;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Service;

import com.jcraft.jsch.Channel;
import com.jcraft.jsch.ChannelExec;
import com.jcraft.jsch.ChannelSftp;
import com.jcraft.jsch.JSch;
import com.jcraft.jsch.JSchException;
import com.jcraft.jsch.Session;

import egovframework.example.sample.restaurant.service.MachineRunningService;
import egovframework.rte.fdl.cmmn.EgovAbstractServiceImpl;

@Service("machineRunningService")
public class MachineRunningServiceImpl extends EgovAbstractServiceImpl implements MachineRunningService {
	
	private static final Logger LOGGER = LoggerFactory.getLogger(MachineRunningServiceImpl.class);
	
	private Session session = null;
	private Channel channel = null;
	private ChannelSftp channelSftp = null;
	
	@Override
	public void runMachineRunning(int sex, int generation) throws Exception {
		//접속정보
		String ip = "192.168.110.115";
		int port = 22;
		String id = "root";
		String pw = "1234";
		
		//명령어
		String cmd1 = "source /etc/profile; ";
		String cmd11 = "cd ~; ";
		
		
		String cmd2 = "cd /home/hdp115/dataTeam; ";
		String cmd3 = "python main.py";
		String arg1 = " " + sex + " ";
		String arg2 = generation + " >> /home/webJh/pythonLog.txt";
		String cmds = cmd1 + cmd11 + cmd2 + cmd3 + arg1 + arg2;
		System.out.println(cmds);
		
		
		JSch jsch = new JSch();
		
		try {
			Session session = jsch.getSession(id, ip, port); //접속아이디, ip, port(int)
	        session.setPassword(pw);
	        
	        java.util.Properties config = new java.util.Properties();
	        config.put("StrictHostKeyChecking", "no");
	        
	        session.setConfig(config);
	        session.connect();  //연결
	        
	        channel = session.openChannel("exec");
    		ChannelExec channelExec = (ChannelExec) channel;
//    		channelExec.setPty(true);
    		channelExec.setCommand(cmds);
    		channelExec.connect();
    		//System.out.println("==> Connected to " + host);
            
    		channel.disconnect();
    	    session.disconnect();
		} catch (JSchException e) {
			System.out.println("jsch에러 : " + e);
		} finally {
			if (channel != null) {
				channel.disconnect();
			}
			if (session != null) {
				session.disconnect();
			}
			
		}
		
		
		Thread.sleep(4000);
        
        
		

        
        
//        //콜백을 받을 준비.
//        StringBuilder outputBuffer = new StringBuilder();
//        InputStream in = channel.getInputStream();
//        ((ChannelExec) channel).setErrStream(System.err);        
//        
//        channel.connect();  //실행
//        
//  
//        byte[] tmp = new byte[1024];
//        while (true) {
//            while (in.available() > 0) {
//                int i = in.read(tmp, 0, 1024);
//                outputBuffer.append(new String(tmp, 0, i));
//                if (i < 0) break;
//            }
//            if (channel.isClosed()) {
//                System.out.println("결과");
//                System.out.println(outputBuffer.toString());
//                channel.disconnect();
//            }
//        }        
    

	}
}
