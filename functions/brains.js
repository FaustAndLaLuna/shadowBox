function toCallAttributes(object){
    let attributes = ` ${object.brightness} ${object.sectionOrder} ${object.funName}`;
    if(typeof object.startColor != 'undefined'){
        object.startColor.forEach((el, i) => {
            attributes += ` [${el}]`;
        });
    }
    if(typeof object.endColor != 'undefined'){
        object.endColor.forEach((el, i) => {
            attributes += ` [${el}]`;
        });
    }
    if(typeof object.speed != 'undefined')
            attributes += ` ${object.speed}`
    return attributes;
}
exports.toCallAttributes = toCallAttributes;