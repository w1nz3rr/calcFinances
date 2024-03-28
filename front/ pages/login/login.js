const form = document.getElementById('login-form')

form.addEventListener("submit", auth)

async function auth(event) {
    event.preventDefault()

    const data = {
        login: document.getElementById('login').value,
        password: document.getElementById('password').value,
    }

    const response = await makeRequest({
        url: 'http://127.0.0.1:5000/api/auth/login',
        method: 'POST',
        body: data,
        hasAuth: false
    })

    if ("error" in response) {
        console.log(response.error)
    } else {
        localStorage.setItem('auth_token', response.token)
        window.location = 'https://google.com'
    }
}