# 이 글은 git clone 으로 접속 후, 환경 설정에 관한 내용입니다.
```
cd ~
mkdir 1st_project
cd 1st_project
git clone https://github.com/checkCJY/confused_project.git

- 아래부터 시작하시면 됩니다.    


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
```