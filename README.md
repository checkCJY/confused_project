# 5조 팀 프로젝트 README 입니다.



### 사용 설명서

```
사용설명서, 흐름대로 명령어 입력

git remote remove origin    
deactivate
> 원격저장소 연결 끊기, 가상환경 종료

git remote -v 
> 연결끊어진 것 확인

cd ~
git clone https://github.com/checkCJY/confused_project.git

cd confused_project
code -r .
-> 현재 vscode 를 confused_project 디렉토리에서 재시작

uv venv
> uv 가상환경 만들기, 깃초기화는 생략

source .venv/bin/activate
uv pip install -r requirements.txt
> 가상환경 실행 및 pip설치

git branch -M main

git remote -v 
> 내용이 나온다면 아래내용 생략. 이미 연결된상태

git remote add origin https://github.com/checkCJY/confused_project.git

# 9. local branch 생성 후 원격 저장소 데이터 받기
git branch develop
git branch feature
git switch develop 
    git pull origin develop
git checkout feature
    git pull origin feature
```

### 사용 기술 / 범위
언어 : Python 3
실행 환경 : WSL + VSCode
버전 관리 : Git / Github + requirement (pip)
UI : Streamlit 기반 표현
데이터 저장 : CSV 파일
구조 :
- app.py : Streamlit 실행 진입점
- inout, data, logic, ui, test : 각각 기능에 맞게 각각 디렉터리 구조

---

### 구현한 기능 
```
F1번 부터 F5번까지 확인
D1번 부터 D4번까지 구현
```

### 아쉬웠던 부분
```
파일 입출력, 또는 계산에서 try-execpt를 사용하지 못함
데이터 파일 백업, 또는 추가 기능은 구현은 해봤으나, 마지막에 담지못함
코드 작성 과정에서 잘게 나누어 디버깅후 진행해야 했으나, 그런 부분이 부족함.
github에 대해서 설명 및 실습과정에서 딜레이가 발생하였다.
코드 리뷰를 디테일하게 진행하지 못한점이 아쉽다.
```

### 디렉토리 내부 구조
```
project(폴더명)
├── app.py 
├── inout
│   └── io_manager.py 
│       # 인풋과 아웃에 관련된 코드가 작성되어 있습니다.
├── data
│   └── data.csv
│       # .ignore로 무시하고 넘어가야 하는 실제 파일입니다.
│       # sample만 올렸어야 했는데 늦게 확인했습니다
├── ui
│   └── ui_manager.py
│       # streamlit을 이용해 화면출력을 위한 코드가 모여있습니다.
├── test
│   └── test_finance.py
│       # logic_manager 의 테스트 내용과 관련된 코드입니다
│       # 프로그램 실행은 프로젝트 폴더에서
│       # python3 -m pytest test/test_finance.py
├── logic
│   └── logic_manager.py
│       # 계산과 관련된 코드들이 들어 있습니다.
├── note
│   └── 개인_참고자료
│        ├── "이니셜"_ref.docx.md   
│        └── 위와 동일한 파일 6개
│   ├── commit_메세지_규칙.md    
│   ├── 깃허브_명령어.md  
│   ├── 초기세팅_설명서.md  
│   ├── 회의내용.md  
│   ├── 참고자료.md       
│   ├── 흐름도_수정본.png 
└── code_history
    # 프로젝트를 진행하면서, 작성해둔 코드들 모음입니다.
```
