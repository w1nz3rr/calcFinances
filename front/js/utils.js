async function makeRequest(request) {
    let headers = {
        'Content-type': 'application/json; charset=UTF-8',
    }

    if (request.hasAuth) headers.Authorization = localStorage.getItem('auth_token')

    let response = await fetch(request.url, {
        method: request.method,
        body: JSON.stringify(request.body),
        headers,
    })

    return await response.json()
}