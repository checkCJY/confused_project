### !!note 폴더에 프로젝트 진행시 읽고 따라주셔야 합니다

---

### 사용 설명서는 맨 아래로 이동해주세요. 

```
# 1. 원격저장소 연결 끊기, 가상환경 종료
git remote remove origin
deactivate

# 1.1 연결끊어진 것 확인
git remote -v 
-> 해당 명령어 입력 후 아무것도 안뜹니다.

# 2. 홈 디렉터리로 이동 후 git clone
cd ~
git clone https://github.com/checkCJY/confused_project.git

# 3. 디렉터리 생성 확인
ls -l
-> confused_project 폴더 생성 확인

# 4. 디렉토리 이동후 vscode 재시작
cd confused_project
pwd
-> 경로 확인해주세요. /home/"여러분이름"/confused_project
code -r .
-> 현재 vscode 를 confused_project 디렉토리에서 재시작

# 5. uv를 이용한 깃초기화(생략), uv 가상환경 만들기
> 생략하는 이유는 pyproject.toml 파일이 있기 때문입니다.
uv venv

# 6. 가상환경 실행 및 pip설치
source .venv/bin/activate
uv pip install -r requirements.txt

# 7. 원격저장소 설정 
git branch -M main
-> git local branch를 main으로 잡겠다.

# 8. 원격저장소 설정
git remote -v 
-> 내용이 나온다면 아래내용 생략. 이미 연결된상태

git remote add origin https://github.com/checkCJY/confused_project.git

# 9. local branch 생성 후 원격 저장소 데이터 받기
git branch develop
git branch feature
git switch develop 
    git pull origin develop
git checkout feature
    git pull origin feature

# 10. 익스텐션에서 해당 확장자 설치 (하신분들은 안하셔도 됩니다.)
Commit Message editor

tip.
    메세지 입력 칸에 마우스를 가져다 대면 연필모양이 나옵니다
    버튼을 누르면 commit 메세지를 길게 작성할 수 있어요
```


### 초기세팅 디렉터리 내부구조 ( #부분은 다들 확인해주세요 )
```
project(폴더명)
├── note
│   └── 개인_참고자료
│        ├── "이니셜"_ref.docx.md   #5.1
│        └── 위와 동일한 파일 6개
│   ├── commit_메세지_규칙.md    #1
│   ├── 깃허브_명령어.md  #2
│   ├── 초기세팅_설명서.md  #3
│   ├── 회의내용.md  #4
│   ├── 참고자료.md       #5
│   └── 흐름도_수정본.png       #6
├── app.py ( #3번 세팅 후 실행, 세팅확인용)
├── code_history ( 추가 )
│   └── 여러가지.py ( 코드 작성하고, push 받은 내용 )
└──  requirements.txt   #7

#1 commit_메세지_규칙
- 반드시 읽어주세요
- commit시 해당 문서의 양식대로 작성
- git pull/push 시 branch 확인 후 진행해야 합니다

#2 깃허브_명령어
- 프로젝트 진행하면서 github 또는 git과 관련된 명령어 모음 문서입니다
- 추가하고 싶은 내용, 또는 알게 된 내용은 작성해주시면 됩니다

#3 초기세팅_설명서
- git clone 후 여러분들이 해야하는 기초세팅입니다
- window 운영체제에서 진행했으므로, mac이신분은 추가로 확인하셔야 합니다

#4 회의내용
- 프로젝트를 진행하면서 의견나눔에 관한 내용을 작성하는 문서입니다.

#5, #5.1 참고자료, 개인_참고자료/"이니셜"_ref.docx.md
- 프로젝트를 진행하면서 검색 또는 AI를 통해 얻은 자료 #4.1에 모아둡니다
- 추후 프로젝트 마무리 단계에서 취합후 #4 에 분류별로 작성합니다

#6 흐름도_수정본
- 제가 이해한 github 내용으로 아키텍쳐를 그려봤습니다.
- 현재 프로젝트 단계에서는 해당 흐름대로 진행 할 예정입니다.

#7 requirements.txt
- 제가 가상환경 세팅 후 설치한 pip 들의 version 입니다
- 확인하고 싶다면 세팅을 끝내 후 다음 명령어를 작성해주세요

# check_req.txt 와 requirements.txt 파일비교
uv pip freeze > check_req.txt

확인 되었으면 check_req.txt는 삭제하세요. 필요 없는 파일입니다.
```