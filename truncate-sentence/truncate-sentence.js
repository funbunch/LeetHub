/**
 * @param {string} s
 * @param {number} k
 * @return {string}
 */
var truncateSentence = function(s, k) {
    // turn s string into array
        let newS = s.split(' ')
        //console.log(newS)
        newS.splice(k)
        return newS.join(' ')
    }

truncateSentence("Hello how are you Contestant",4)