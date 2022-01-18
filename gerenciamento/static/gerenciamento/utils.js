const eventCreateButton = (button, fields) => {
    button.addEventListener('click', event => {
        event.preventDefault()
        button.removeEventListener()
        const caption = button.closest('caption')
        const table = button.closest('table')
        const tbody = table.querySelector('tbody')

        changeMethod('', event.target)
        button.remove()

        // Generate Cancel Button
        const cancelButton = generateButton(false, 'danger', 'botao-cancelar-criacao', 'Cancelar')

        // Insert Cancel Button
        caption.appendChild(cancelButton)

        // Generate Table Row
        const tableRow = generateTableRows(fields, names)

        // Insert Table Row
        tbody.appendChild(tableRow)
    })
}

const generateTableRows = (fields, names) => {
    const tr = document.createElement('tr')

    for (let index = 0; index < fields; index++) {
        const td = document.createElement('td')
        td.innerHTML = `
            <input type="text" class="form-control" name=${names[index]}>
            `
        tr.appendChild(td)
    }

    const td = document.createElement("td")
    const submitButton = generateButton('submit', 'success', 'botao-enviar w-100', 'Enviar')
    td.appendChild(submitButton)
    tr.appendChild(td)
    return tr
}

const generateButton = (type, color, classes, value) => {
    const button = document.createElement('button')
    if (type) button.setAttribute('type', `${type}`)
    button.setAttribute('class', `btn btn-${color} ${classes}`)
    button.innerText = value

    return button
}