# !!note 폴더에 프로젝트 진행시 읽고 따라주셔야 합니다

---

# 이 글은 git clone 으로 접속 후, 환경 설정에 관한 내용입니다.

```
!!! vscode 실행 후, 가상환경이 켜져있다면 다음 명령어
deactivate 

# 가상환경이 꺼진 후 terminal에서 명령어 작성
cd ~
mkdir 1st_project
cd 1st_project
git clone https://github.com/checkCJY/confused_project.git   

# uv 실행 전 상태확인
uv --version
uv venv

!!! 가상환경 켜진 상태를 확인
source .venv/bin/activate

git branch -M main
# 원격저장소 설정
git remote add origin https://github.com/checkCJY/confused_project.git

# github 설치환경과 동일하게 pip설치
uv pip install -r requirements.txt

+ 익스텐션에서 해당 확장자 설치
Commit Message

메세지 입력 칸에 마우스를 가져다 대면 연필모양이 나옵니다
버튼을 누르면 commit 메세지를 길게 작성할 수 있어요

세팅완료

```


### 초기세팅 디렉터리 내부구조 ( #부분은 다들 확인해주세요 )
```
project(폴더명)
├── note
│   └── ref_docx
│        ├── "이니셜"_ref.docx.md   #5.1
│        └── 위와 동일한 파일 6개
│   ├── commit_message_rules.md    #1
│   ├── github_command.md  #2
│   ├── setting_manual.md  #3
│   ├── mom.md  #4
│   ├── reference.md       #5
│   └── 흐름도_수정본.png       #6
├── app.py ( #3번 세팅 후 실행, 세팅확인용)
├── main.py ( 기본으로 있던 py )
└──  requirements.txt   #7

#1 commit_message_rules
- 반드시 읽어주세요
- commit시 해당 문서의 양식대로 작성
- git pull/push 시 branch 확인 후 진행해야 합니다

#2 github_command
- 프로젝트 진행하면서 github 또는 git과 관련된 명령어 모음 문서입니다
- 추가하고 싶은 내용, 또는 알게 된 내용은 작성해주시면 됩니다

#3 setting_manual
- git clone 후 여러분들이 해야하는 기초세팅입니다
- window 운영체제에서 진행했으므로, mac이신분은 추가로 확인하셔야 합니다

#4 mom
- 프로젝트를 진행하면서 의견나눔에 관한 내용을 작성하는 문서입니다.

#5, #5.1 reference, "이니셜"_ref.docx.md
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