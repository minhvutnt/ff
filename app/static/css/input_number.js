function input_2digit(element){
    element.oninput = (e) => {
      const value = element.value;

      let [_, sign, integer, decimals] = value.replace(/[^\d\.\-]/g, "") // invalid characters
        .replace(/(\..*?)\./g, "$1") 
        .replace(/(.+)-/g, "$1")
        .match(/^(-?)(.*?)((?:\.\d*)?)$/);

      let pos = element.selectionStart - 1;
      if(!integer && decimals) pos += 2;
      if(integer || decimals) {

        integer = +integer;
        try{
            newdecimals = decimals.toString()[0] + decimals.toString()[1]+ decimals.toString()[2];
            if(!isNaN(newdecimals)){
                decimals = newdecimals;
            }
        }catch (e) {
        }
      }

      const formatted = sign + integer + decimals;

      if(formatted !== value) {
        element.value = formatted;
      }
    }
}