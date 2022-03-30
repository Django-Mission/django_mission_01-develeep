from django.shortcuts import render


# Create your views here.


def lotto_index(request):

    return render(request, 'lotto_index.html')


def lotto_result(request):
    import random

    lotto_number = list()
    # 게임 수 받기
    game = int(request.GET.get('game', 1))
    # 1~46 숫자 배열
    pull_number = list(index for index in range(1, 46))

    # 게임 수만큼 로또 번호 추출
    for _ in range(game):
        # random.sample을 통해 1~46의 숫자중 6개를 추출
        lotto_number.append(random.sample(pull_number, 6))

    return render(request, 'lotto_result.html', {'lotto_number': lotto_number, 'game': game})
