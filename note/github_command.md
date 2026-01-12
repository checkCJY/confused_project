### 이 문서는 github 명령어 모음입니다
**수정이 있거나, 추가를 원하면 말씀 해 주세요**

### !!! 반드시 git pull / push 시 branch 확인하세요
### 확인 안하고 pull / push 하면, 로컬 또는 원격 branch 내용이 달라집니다.

```
흐름 설명 
1. 로컬 branch를 생성한다 main / develop
    branch 생성 및 이동 명령어 확인
2. 로컬 branch에 원격 저장소 내용을 받는다 (pull)
    (origin/main -> local-/main develop에서도 동일하게. )
3. 로컬 branch에서 작업한다. 
    local/feature 생성 후 작업추천
    이유 : local/develop을 자주 pull 해두고, 따로 관리하면 오류발생 확률 적음
4. 작업한 내용을 원격 저장소에 올린다(push) 
    (local/feature -> origin/develop)
5. 원격 저장소에 모든 내용이 저장이 확인되면, 다시 pull로 개발환경을 맞춘다
    (origin/develop -> local/develop)
6. 개발을 끝내고 version이 완성되면, origin/main 에 push 또는 merge를 통해 병합.
    !! 이 6번 과정은 한명만 해도 상관 없습니다. 
    !! 아마 팀장인 제가 하거나, 다른 분께 부탁할 수 있어요
7. 처음 local branch 개발환경과 원격 저장소 branch들의 내용이 다르므로
   2번으로 돌아가서 local branch와 origin branch의 상태를 맞추기 위해 git pull한다
```


브랜치 확인 필수
    명령어를 치기 전에 항상 git branch를 입력해 내가 지금 어느 브랜치에 있는지 확인하세요.
Pull 먼저, Push 나중에
    원격에 올리기 전에는 항상 pull을 먼저 받아보는 습관을 들이면 충돌을 줄일 수 있습니다.
커밋은 작게 
    한 번에 너무 많은 코드를 커밋하면 나중에 수정하기 힘듭니다. 기능 단위로 쪼개서 커밋하세요.

tip.1   git pull 하기 전, local branch 에서 commit을 완료 해두면 안전하다.
tip.2   충돌을 두려워하지 말자.
        코드가 겹치면 git이 알려주는 안전장치 입니다.
        충돌하면 다같이 해결합시다.


4-5번에서 원래 PR 과정을 해야하는데, 생략합니다.
대신 원격 저장소 branch (origin/develop) 에 push하면
반드시 전체에게 알려줘야 합니다.
그래야 다른 사람들이 pull로 받을 수 있어요.

```
# 메인 브랜치로 이동 및 최신화
git checkout develop
git pull origin develop

# develop 브랜치로 이동
git checkout develop
git switch develop

# 혹시 모를 업데이트 확인
git pull origin develop

# 이 과정이 오류를 줄이는 방법입니다.
# 새 기능 브랜치 생성 및 이동(이름은 자유롭지만 기능 위주로)
git checkout -b feature/login-page

# 내 기능 브랜치를 원격에 전송
git push origin develop

# 최신 코드 가져오기 (충돌 방지용)
# 현재 내 기능 브랜치에서 실행 (feature/login-page)
git pull origin develop



6. 실수했을 때 긴급 처방
# 1. 방금 한 커밋 메시지를 수정하고 싶을 때 (질문 안하셔도 됩니다)
git commit --amend -m "수정할 메시지"

# 2. 병합 중 충돌이 너무 심해서 일단 취소하고 싶을 때
git merge --abort

# 3. 수정한 내용을 다 버리고 마지막 커밋 상태로 되돌리고 싶을 때
git checkout -- .

```