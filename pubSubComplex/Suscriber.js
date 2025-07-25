import Debouncer from Debouncer;
class Subscriber{

    constructor(topics){
        this.topic = topics || {}
        this.subscriptions = {}
    }
    subscribe(path,callback){
        // register the subscriber to a path of data
//storing our subscription path allows us to define an easy mechanism for notifying multiple subscribers regarding changes to a path of information
        let subpath = path.join("-");

//storing metadata and accessor functions in the subscription object means that we can pass this reference
//to the subscribing function as well as to the subscriptions member without having to remember any path information.
//We can embed our unsubscribe and publish logic directly passing only the absolutely necessary information.

        let uniqId = this.uuidv4();

        var subscription = {
            id:uniqId,
            callback:callback
            unsubscribe:()=>{
            this.unsubscribe(subpath,uniqId);},
            publish:(data)=> {
            this.publish(path,data);},
            get:()=>{
            return this.pluck(this.topic,path);}
        }

        if(subpath in this.subscriptions){
            this.subscriptions[subpath].push(subscription);
        }else{
            this.subscriptions[subpath]=[subscription];
            this.subscriptions[subpath].debouncer = new Debouncer();
        }

        return subscription;
    }
    unsubscribe(path,uniqId){
        // remove the subscribtion to a path of data
        let removeAt=this.subscriptions[subpath].findIndex((subscription) =>{
                return subscription.id === uniqId
            });

        if (Array.isArray(this.subscriptions[subpath])) {
            if (this.subscriptions[subpath].length === 1 && removeAt >= 0) {
                 delete this.subscriptions[subpath]; // Delete the entire array

            } else{
                if (removeAt >= 0 && removeAt < this.subscriptions[subpath].length) {
                    this.subscriptions[subpath].splice(removeAt, 1); // Remove the item at removeAt
                }
            }

        }


    }
    get(path){
        // get data at some path
        this.pluck(this.topic,path)
    }
    publish(path,data){
        // mutate and notify subscribers of a change
        Object.assign(this.pluck(this.topic,path),data);

        this.subscriptions[path.join("-")].debouncer.debounce(()=>
        {
            this.subscriptions[path.join("-")].forEach((subscription)=>{
                subscription.callback(this.pluck(this.topic,path),subscription);
            });
        })

    }

    uuidv4(){
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
            var r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);
            return v.toString(16);
        });
    }

    pluck(data,path,set=null){
        if(path.length > 1){
            return this.pluck(data[path[0]],path.slice(1,path.length), set);
        }else{
            if(path.length == 0 ){
                return data;
            }else{
                if(set == null){
                    return data[path[0]];
                }else{
                    data[path[0]]=set;
                    return data[path[0]];
                }
            }
        }

    }
   export default Subscriber

}



