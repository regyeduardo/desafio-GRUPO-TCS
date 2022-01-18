// const getAllSiblings = (elem) => {
//     const siblings = [];

//     if (!elem.parentNode) {
//         return siblings;
//     }

//     let sibling = elem.parentNode.firstElementChild;

//     do {
//         if (sibling != elem) {
//             siblings.push(sibling);
//         }
//     } while (sibling = sibling.nextElementSibling);

//     return siblings;
// };

// // Editado
// const insertEditIcon = formControl => {
//     const inputGroup = formControl.closest('.input-group')
//     const editIcon = generateEditAndSendIcons('edit')
//     insertElement(inputGroup, editIcon, '.input-group-append', 'appendChild')
// }

// // Edited

// const removeSendIcon = formControl => {
//     const inputGroup = formControl.closest('.input-group')
//     const inputGroupAppend = inputGroup.querySelector('.input-group-append')
//     if (inputGroupAppend) {
//         inputGroupAppend.remove()
//         return true
//     }

//     return false
// }

// const checkIfAtLeast2FieldsInTheRowHaveBeenEdited = formControl => {
//     const tr = formControl.closest('tr')
//     const formControls = Array.prototype.slice.call(tr.querySelectorAll('.form-control'))
//     const editedFields = formControls.reduce((acc, nestedFormControl) => {
//         if (checkIfInputValueWasEdited(nestedFormControl)) return acc += 1
//         return acc
//     }, 0)

//     if (editedFields >= 2) return true
//     return false
// }

// const addDeleteButton = formControl => {
//     const tr = formControl.closest('tr')
//     const deleteButton = tr.querySelector('.botao-apagar')

//     if (!deleteButton) {
//         const td = document.createElement("td")
//         td.innerHTML = `
//             <button type="submit" class="btn btn-danger botao-apagar w-100">Apagar</button>
//             `
//         const trChildren = Array.prototype.slice.call(tr.children)
//         tr.appendChild(td)
//         addEventDeleteButton(tr.querySelector('.botao-apagar'))
//     }
// }

// // Edited
// const insertUpdateButton = formControl => {
//     const tr = formControl.closest('tr')
//     const td = document.createElement("td")
//     td.appendChild(generateButton('submit', 'success', 'botao-atualizar', 'w-100', 'Atualizar'))
//     insertElement(tr, td, '.botao-atualizar', 'appendChild')
// }

// const removeUpdateButton = formControl => {
//     const tr = formControl.closest('tr')
//     const updateButton = tr.querySelector('.botao-atualizar')

//     if (updateButton) {
//         const td = updateButton.parentElement
//         td.remove()
//         return true
//     }
//     return false
// }

// const insertEditIconInEditedFields = formControl => {
//     const td = formControl.closest('td')
//     const tdSiblings = getAllSiblings(td)

//     tdSiblings.forEach(sibling => {
//         const siblingInput = sibling.querySelector('.form-control')

//         if (siblingInput) {
//             const siblingInputWasEdited = checkIfInputValueWasEdited(siblingInput)

//             if (siblingInputWasEdited) {
//                 insertSendIcon(siblingInput)
//                 createEventEditButton(siblingInput)
//             }
//         }

//     })
// }

// const generateConfirmationCard = action => {
//     const templateCollapse = `
//                 <p class="text-center">Tem certeza que deseja ${action}?</p>
//                 <div class="btn-toolbar mb-3 d-flex justify-content-center">
//                     <div class="btn-group mr-2">
//                         <button type="submit" class='btn btn-secondary allow'>SIM</button>
//                     </div>
//                     <div class="btn-group mr-2">
//                         <button type="button" class='btn btn-primary denied'>NAO</button>
//                     </div>
//                 </div>
//             `

//     const card = document.createElement('div')
//     card.setAttribute('class', 'card card-body')
//     card.innerHTML = templateCollapse

//     return card
// }

// // Editado
// const insertConfirmationButtons = (td, verb) => {
//     if (!td.querySelector('.card')) {
//         const card = generateConfirmationCard(verb)
//         td.appendChild(card)
//     }
// }

// // UPDATES
// const setHiddenInput = (where, action) => {
//     const hiddenInputs = Array.prototype.slice.call(where.querySelectorAll('.hidden_id'))

//     hiddenInputs.forEach(hiddenInput => {
//         if (action === 'setDisabled') hiddenInput.setAttribute('disabled', '')
//         else if (action === 'removeDisabled') hiddenInput.removeAttribute('disabled')
//     })
// }

// const insertElement = (where, element, findForSelector, action) => {
//     if (!where.querySelector(`${findForSelector}`)) {
//         if (action == 'appendChild') where.appendChild(element)
//     }
// }

// const generateButton = (type, color, className, width, name) => {
//     const button = document.createElement('button')
//     if (type) button.setAttribute('type', `${type}`)
//     button.setAttribute('class', `btn btn-${color} ${className} ${width}`)
//     button.innerText = name

//     return button
// }

// const generateTr = fields => {
//     const tr = document.createElement('tr')

//     for (let index = 0; index < fields.length - 1; index++) {
//         const name = fields[index].innerText.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, "");
//         const td = document.createElement('td')
//         td.innerHTML = `
//             <input type="text" class="form-control" name=${name}>
//             `
//         tr.appendChild(td)
//     }

//     const td = document.createElement("td")
//     td.appendChild(generateButton('submit', 'success', 'botao-enviar', 'w-100', 'Enviar'))
//     tr.appendChild(td)
//     return tr
// }


// // END UPDATES

// const createEventConfirmationButtonsUpdate = formControl => {
//     const tr = formControl.closest('tr')
//     const tbody = formControl.closest('tbody')
//     const deniedButton = tr.querySelector('.denied')
//     deniedButton.addEventListener('click', ev => {
//         deniedButton.removeEventListener('click', () => { })
//         ev.preventDefault()
//         const nestedCard = deniedButton.closest('.card')

//         reInsertAllIcons(tbody)
//         setAttributeDisabled(tbody, '.hidden_id')
//         removeAttributeDisabled(deniedButton.closest('table'), '.btn')
//         nestedCard.remove()

//     })
// }

// const createEventConfirmationButtonDelete = element => {
//     element.addEventListener('click', (event) => {
//         element.removeEventListener('click', () => { })
//         event.preventDefault()
//         const form = element.closest('form')
//         const inputMethod = form.querySelector('[value=DELETE]')
//         inputMethod.setAttribute('value', 'PUT')
//         setAttributeDisabled(form, '.hidden_id')
//         removeAttributeDisabled(form, '.btn')
//         reInsertAllIcons(form)
//         const nestedCard = element.closest('.card')
//         nestedCard.remove()
//     })
// }

// const createEventEditButton = formControl => {
//     const inputGroupAppend = formControl.nextElementSibling
//     inputGroupAppend.addEventListener('click', (e) => {
//         inputGroupAppend.removeEventListener('click', () => { })
//         removeElement(formControl.closest('tbody'), '.input-group-append')
//         setAttributeDisabled(formControl.closest('tbody'), '.form-control', formControl)
//         const hiddenIdCurrentRow = formControl.closest('tr').querySelector('.hidden_id')
//         hiddenIdCurrentRow.removeAttribute('disabled')
//         setAttributeDisabled(formControl.closest('tbody'), '.hidden_id', hiddenIdCurrentRow)
//         setAttributeDisabled(formControl.closest('table'), '.btn', formControl.closest('tr').querySelector('.btn'))
//         insertConfirmationButtons(formControl.closest('td'), 'atualizar')
//         createEventConfirmationButtonsUpdate(formControl)
//     })
// }

// const createEventClickEditIcon = formControl => {
//     const inputGroupAppend = formControl.nextElementSibling
//     const inputGroupText = inputGroupAppend.firstElementChild
//     inputGroupText.addEventListener('click', (event) => {
//         inputGroupText.removeEventListener('click', () => { })
//         inputGroupAppend.remove()
//         formControl.removeAttribute('disabled')
//         formControl.focus()
//     })
// }

// const createEventFocusOutInput = formControl => {
//     formControl.addEventListener('focusout', (event) => {
//         const target = event.target
//         formControl.removeEventListener('focusout', () => { })
//         const inputWasEdited = checkIfInputValueWasEdited(target)

//         if (inputWasEdited) {
//             const atLeast2FieldsWereEdited = checkIfAtLeast2FieldsInTheRowHaveBeenEdited(target)

//             if (atLeast2FieldsWereEdited) {
//                 removeElement(target.closest('tr'), '.botao-apagar', 'removeParent')
//                 insertUpdateButton(target)
//                 removeElement(target.closest('tr'), '.input-group-append')
//             } else {
//                 insertSendIcon(target)
//                 createEventEditButton(target)
//             }
//         } else {
//             removeSendIcon(target)
//             if (removeUpdateButton(target)) {
//                 addDeleteButton(target)
//                 insertEditIconInEditedFields(target)
//             }
//             insertEditIcon(target)
//             target.setAttribute('disabled', '')
//             createEventClickEditIcon(target)
//         }

//     })
// }

// const formControls = Array.prototype.slice.call(document.querySelectorAll('input.form-control'))

// formControls.forEach(formControl => {
//     createEventClickEditIcon(formControl)
//     createEventFocusOutInput(formControl)
// });

// const addEventAbortCreateButton = abortCreateButton => {
//     abortCreateButton.addEventListener('click', event => {
//         abortCreateButton.removeEventListener('click', () => { })
//         event.preventDefault()
//         const table = abortCreateButton.closest('table')
//         const thead = table.querySelector('thead')
//         const tbody = table.querySelector('tbody')
//         const createButton = generateButton(false, 'primary', 'botao-criar', '', 'Criar')
//         const form = table.closest('form')
//         const inputMethod = form.querySelector('[name=_method]')
//         inputMethod.setAttribute('value', 'PUT')
//         const tr = tbody.lastElementChild
//         tr.remove()
//         abortCreateButton.parentElement.remove()
//         const caption = document.createElement('caption')
//         caption.appendChild(createButton)
//         table.insertBefore(caption, thead)
//         addEventCreateButton(table.querySelector('.botao-criar'))
//         removeAttributeDisabled(tbody, '.btn')
//         reInsertAllIcons(tbody)
//     })
// }

// const addEventCreateButton = createButton => {
//     createButton.addEventListener('click', (event) => {
//         createButton.removeEventListener('click', () => { })
//         event.preventDefault()
//         const table = createButton.closest('table')
//         const thead = table.querySelector('thead')
//         const tbody = table.querySelector('tbody')
//         const fields = thead.firstElementChild.children
//         const form = table.closest('form')
//         const inputMethod = form.querySelector('[value=PUT]')
//         inputMethod.removeAttribute('value')
//         removeElement(tbody, '.input-group-append')
//         setAttributeDisabled(tbody, '.form-control')
//         tbody.appendChild(generateTr(fields))
//         createButton.parentElement.remove()
//         const abortCreateButton = generateButton(false, 'danger', 'botao-cancelar-criacao', '', 'Cancelar')
//         const caption = document.createElement('caption')
//         caption.appendChild(abortCreateButton)
//         table.insertBefore(caption, thead)
//         setAttributeDisabled(tbody, '.btn', table.querySelector('.botao-enviar'))
//         addEventAbortCreateButton(table.querySelector('.botao-cancelar-criacao'))
//     })
// }

// const addEventDeleteButton = deleteButton => {
//     deleteButton.addEventListener('click', event => {
//         event.preventDefault()
//         deleteButton.removeEventListener('click', () => { })
//         const form = deleteButton.closest('form')
//         const tr = deleteButton.closest('tr')
//         const hiddenInput = tr.querySelector('.hidden_id')
//         hiddenInput.removeAttribute('disabled')
//         setAttributeDisabled(form, '.hidden_id', hiddenInput)
//         const inputMethod = form.querySelector('[value=PUT]')
//         inputMethod.setAttribute('value', 'DELETE')
//         setAttributeDisabled(form, '.btn', deleteButton)
//         removeElement(deleteButton.closest('tbody'), '.input-group-append')
//         insertConfirmationButtons(deleteButton.closest('td'), 'deletar')
//         createEventConfirmationButtonDelete(deleteButton.closest('td').querySelector('.denied'))
//     })
// }

// const deleteButtons = Array.prototype.slice.call(document.querySelectorAll('.botao-apagar'))

// deleteButtons.forEach(deleteButton => {
//     addEventDeleteButton(deleteButton)
// });


/////////////
const checkIfInputValueWasEdited = formControl => {
    if (formControl.value != formControl.getAttribute('curValue')) return true
    return false
}

const howMuchFormControlsHaveBeenEdited = element => {
    const tr = element.closest('tr')
    const formControls = Array.prototype.slice.call(tr.querySelectorAll('.form-control'))
    const editedFields = formControls.reduce((acc, nestedFormControl) => {
        if (checkIfInputValueWasEdited(nestedFormControl)) return acc += 1
        return acc
    }, 0)

    return editedFields
}

const generateIcon = icon => {
    const inputGroupAppend = document.createElement("SPAN")
    inputGroupAppend.setAttribute("class", "input-group-append")

    if (icon == 'send') {
        inputGroupAppend.innerHTML = `<i class="input-group-text bi bi-send"></i>`
    } else {
        inputGroupAppend.innerHTML = `<i class="input-group-text bi bi-pencil-square"></i>`
    }
    const inputGroupText = inputGroupAppend.querySelector('.input-group-text')
    eventEditIcon(inputGroupText)
    return inputGroupAppend
}


const removeElement = (where, selector, action) => {
    const elements = Array.prototype.slice.call(where.querySelectorAll(`${selector}`))

    elements.forEach(element => {
        if (action === 'removeParent') {
            element.parentElement.remove()
        } else element.remove()
    })
}

const setAttributeDisabled = (where, selector, exception, exceptionType) => {
    const elements = Array.prototype.slice.call(where.querySelectorAll(`${selector}`))

    elements.forEach(element => {
        if (exception) {
            if (exceptionType == 'element') {
                if (!element.isEqualNode(exception)) element.setAttribute('disabled', '')
            } else {
                if (!element.closest('tr').isEqualNode(exception.closest('tr'))) element.setAttribute('disabled', '')
            }
        } else element.setAttribute('disabled', '')
    })
}

const removeAttributeDisabled = (where, selector, exception) => {
    const elements = Array.prototype.slice.call(where.querySelectorAll(`${selector}`))

    elements.forEach(element => {
        if (exception) {
            if (!element.isEqualNode(exception)) element.removeAttribute('disabled')
        } else element.removeAttribute('disabled')
    })
}

const reInsertAllIcons = tbody => {
    const formControls = Array.prototype.slice.call(tbody.querySelectorAll('.form-control'))

    formControls.forEach(nestedFormControl => {
        const inputWasEdited = checkIfInputValueWasEdited(nestedFormControl)

        if (inputWasEdited) {
            nestedFormControl.parentElement.appendChild(sendIcon)
            eventFocusOut(nestedFormControl)
            if (nestedFormControl.hasAttribute('disabled')) nestedFormControl.removeAttribute('disabled')
        } else {
            const editIcon = generateIcon('edit')
            nestedFormControl.parentElement.appendChild(editIcon)
        }
    })
}

const eventFocusOut = formControl => {
    formControl.addEventListener('focusout', event => {
        event.preventDefault()
        formControl.removeEventListener('focusout', () => {})

        const tableRow = formControl.closest('tr')
        const hiddenId = tableRow.querySelector('.hidden_id')
        const tbody = tableRow.closest('tbody')
        const form = tbody.closest('form')
        const editedFormControlsInTheRow = howMuchFormControlsHaveBeenEdited(formControl)

        if (editedFormControlsInTheRow >= 1) {
            const deleteButton = tableRow.querySelector('.botao-apagar')
            hiddenId.removeAttribute('disabled')
            setAttributeDisabled(tbody, '.form-control', formControl, 'row')
            if (deleteButton) {
                const td = deleteButton.closest('td')
                deleteButton.remove()
                const divFlex = document.createElement('div')
                divFlex.setAttribute('class', 'enviar-reverter d-flex flex-row justify-content-center flex-nowrap')
                divFlex.innerHTML = `
                    <button type="submit" class="btn btn-info botao-cancelar-mudancas w-100 mr-2">Reverter</button>
                    <button type="submit" class="btn btn-success botao-enviar w-100">Enviar</button>
                `
                td.appendChild(divFlex)
                setAttributeDisabled(tbody, '.btn', tableRow.querySelector('.btn'), 'row')
                setAttributeDisabled(form.querySelector('caption'), '.btn')
                const botaoCancelarMudancas = divFlex.querySelector('.botao-cancelar-mudancas')

                botaoCancelarMudancas.addEventListener('click', e => {
                    botaoCancelarMudancas.removeEventListener('click', () => {})
                    e.preventDefault()
                    const formControls = tableRow.querySelectorAll('.form-control')
                    formControls.forEach(nestedFormControl => {
                        if (checkIfInputValueWasEdited(nestedFormControl)) {
                            nestedFormControl.value = nestedFormControl.getAttribute('curValue')
                            nestedFormControl.setAttribute('disabled', '')
                            const editIcon = generateIcon('edit')
                            nestedFormControl.parentElement.appendChild(editIcon)
                        }
                        hiddenId.setAttribute('disabled', '')
                        td.innerHTML = ''
                        td.appendChild(deleteButton)
                        removeAttributeDisabled(form, '.btn')
                        eventDeleteButton(deleteButton)
                    })
                })

            }

            if (!checkIfInputValueWasEdited(formControl)) {
                if (!formControl.closest('td').querySelector('.input-group-append')) {
                    const editIcon = generateIcon('edit')
                    formControl.parentElement.appendChild(editIcon)
                    formControl.setAttribute('disabled', '')
                }
            }
        } else {
            if (!formControl.closest('td').querySelector('.input-group-append')) {
                const editIcon = generateIcon('edit')
                formControl.parentElement.appendChild(editIcon)
                formControl.setAttribute('disabled', '')
            }

            const enviarReverter = tableRow.querySelector('.enviar-reverter')
            if (enviarReverter) {
                const td = enviarReverter.closest('td')
                enviarReverter.remove()
                td.innerHTML = `<button class="btn btn-danger botao-apagar w-100 ${hiddenId.value}">Apagar</button>`
                removeAttributeDisabled(form, '.btn')
                const deleteButton = td.querySelector('.botao-apagar')
                eventDeleteButton(deleteButton)
            }
        }
    })
}

const eventDeleteButton = deleteButton => {
    deleteButton.addEventListener('click', event => {
        // event.preventDefault()
        deleteButton.removeEventListener('click', ()=>{})
        const tr = deleteButton.closest('tr')
        const hiddenId = tr.querySelector('.hidden_id')
        hiddenId.removeAttribute('disabled')
        const form = tr.closest('form')
        form.querySelector('[name=_method]').setAttribute('value','DELETE')
    })
}

const eventEditIcon = editIcon => {
    editIcon.addEventListener('click', event => {
        editIcon.removeEventListener('click', () => { })
        event.preventDefault()
        const formControl = editIcon.closest('.input-group').querySelector('.form-control')
        formControl.removeAttribute('disabled')
        editIcon.parentElement.remove()
        formControl.focus()
        eventFocusOut(formControl)
    })
}

const eventCancelButton = (button, fields, names, disabledIndex) => {
    button.addEventListener('click', event => {
        event.preventDefault()
        button.removeEventListener('click', () => {})
        const caption = button.closest('caption')
        const table = button.closest('table')
        const tbody = table.querySelector('tbody')

        changeMethod(event.target, 'PUT')
        button.remove()

        const createButton = genButton(false, 'primary', 'botao-criar ml-3', 'Criar')
        eventCreateButton(createButton, fields, names, disabledIndex)
        caption.appendChild(createButton)

        tbody.lastElementChild.remove()
        reInsertAllIcons(tbody)
        removeAttributeDisabled(tbody, '.btn')

    })
}

const eventCreateButton = (button, fields, names, disabledIndex) => {
    button.addEventListener('click', event => {
        event.preventDefault()
        button.removeEventListener('click', ()=>{})
        const caption = button.closest('caption')
        const table = button.closest('table')
        const tbody = table.querySelector('tbody')

        changeMethod(event.target, '')
        button.remove()

        const cancelButton = genButton(false, 'danger', 'botao-cancelar-criacao ml-3', 'Cancelar')
        eventCancelButton(cancelButton, fields, names, disabledIndex)
        caption.appendChild(cancelButton)

        removeElement(tbody, '.input-group-append')
        setAttributeDisabled(tbody, '.btn', cancelButton, 'element')

        const tableRow = generateTableRows(fields, names, disabledIndex)
        tbody.appendChild(tableRow)
    })
}

const changeMethod = (element, value) => {
    const form = element.closest('form')
    const method = form.querySelector('[name=_method]')
    method.setAttribute('value', value)
}

const generateTableRows = (fields, names, disabledIndex) => {
    const tr = document.createElement('tr')
    for (let index = 0; index < fields; index++) {
        const td = document.createElement('td')
        td.innerHTML = `
            <input type="text" class="form-control" name=${names[index]} ${disabledIndex == index ? 'disabled' : 'required'}>
            `
        tr.appendChild(td)
    }

    const td = document.createElement("td")
    const submitButton = genButton('submit', 'success', 'botao-enviar w-100', 'Enviar')
    td.appendChild(submitButton)
    tr.appendChild(td)
    return tr
}

const genButton = (type, color, classes, value) => {
    const button = document.createElement('button')
    if (type) button.setAttribute('type', `${type}`)
    button.setAttribute('class', `btn btn-${color} ${classes}`)
    button.innerText = value
    return button
}

const createButtons = Array.prototype.slice.call(document.querySelectorAll('.botao-criar'))

createButtons.forEach(createButton => {
    if (createButton.classList.contains('status')) {
        eventCreateButton(createButton, 2, ['codigo', 'nome'])
    } else eventCreateButton(createButton, 2, ['nome'], 1)
})

const editIcons = Array.prototype.slice.call(document.querySelectorAll('.bi-pencil-square'))

editIcons.forEach(editIcon => {
    eventEditIcon(editIcon)
})

const deleteButtons = Array.prototype.slice.call(document.querySelectorAll('.botao-apagar'))

deleteButtons.forEach(deleteButton => {
    eventDeleteButton(deleteButton)
})