function solution(dirs) {
    let x = 0;
    let y = 0;

    const visited = {};
    let answer = 0;

    for (let dir of dirs) {
        let nx = x;
        let ny = y;

        // 다음 좌표 계산: [y][x] 기준
        if (dir === "U") ny--;       // 위쪽
        else if (dir === "D") ny++;  // 아래쪽
        else if (dir === "L") nx--;  // 왼쪽
        else if (dir === "R") nx++;  // 오른쪽

        // 지도 범위를 벗어나면 이동하지 않음
        if (nx < -5 || nx > 5 || ny < -5 || ny > 5) {
            continue;
        }

        // 현재 위치 -> 다음 위치
        let key1 = `${x},${y}-${nx},${ny}`;

        // 다음 위치 -> 현재 위치 (반대 방향)
        let key2 = `${nx},${ny}-${x},${y}`;

        // 양방향 모두 방문한 적이 없으면 새로운 길
        if (!visited[key1] && !visited[key2]) {
            visited[key1] = true;
            visited[key2] = true;
            answer++;
        }

        // 현재 위치 갱신
        x = nx;
        y = ny;
    }

    return answer;
}