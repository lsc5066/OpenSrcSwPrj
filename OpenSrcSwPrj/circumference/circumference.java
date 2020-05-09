package circumference;

public class circumference {
	public static void main(String[] args) {
		double pi=0;
		int sign=4;
		int n=1000000;
		
		for(int i=0,j=1;i<n;i++,j+=2,sign*=-1)
			pi+=(double)sign/j;
		System.out.printf("라이프니츠 급수를 이용해 구한 원주율 값 : %f",pi);
	}

}
