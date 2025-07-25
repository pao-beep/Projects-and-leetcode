class Debouncer{
    constructor(delay){
        this.callStack=0;
        this.delay=delay || 20;
        this.timeoutId = null;
    }
    debounce(logic){
        this.callStack+=1;
        clearTimeout(this.timeoutId); // Clear the previous timeout

        this.timeoutId =setTimeout(() =>{
            this.callStack-=1;
            this.callStack==0 && logic()
        },this.delay);
    }
}
export default Debouncer;