## inc_dec_table.py

### 증감표

##### 1. 증감표에 f'(x)=0 인 x values와 f(x), f'(x)를 입력하면 증감표를 얻을 수 있다.

##### 2. 입력한 x values의 좌우에서 그래프가 증가, 감소하는지 확인 할 수 있다.

##### 3. f(x) 함수는 연속해야 한다.

##### 4. 증감표를 이용하면 f(x)에 대한 그래프 개형을 그릴 수 있다.

##### 5. 단, f(x)와 f'(x)를 입력 시 sympy가 인식할 수 있는 형태이어야 한다.
	ex) 2*x***3 + x**2 + 3
    사용 가능 변수 x, y, a, b, c, m, n

##### 6. Requirments
	sympy
    python3.6 이상
    
##### 7. 실행법
	python inc_dec_table.py
    
    나오는 입력창에 인수 입력
    
    예) 
    x1 = 2
    x2 = 0
    x3 = (엔터)
    write fx
    : x**3 - x**2 + 1
    write fx PRIME
    : 3*x**2 - 2*x
    
    결과값 출력
    
