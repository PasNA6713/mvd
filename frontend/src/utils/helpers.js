export function formatedDateTime(val) {
    let d = new Date(val)
    
    let day = d.getDate()
    if (day < 10) day = '0' + day

    let month = d.getMonth() + 1
    if (month < 10) month = '0' + month

    let min = d.getMinutes()
    if (min < 10) min = '0' + min

    let hour = d.getHours()
    if (hour < 10) hour = '0' + hour

    return day + "." + month + "." + d.getFullYear() + " в " + hour+ ":" + min
}