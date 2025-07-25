import Subscriber from './services/subscriber.js';
import Debouncer from './services/debouncer.js';

const PubSubService = new Subscriber(topics);


function main(){
    /* Initial Binds */
    bindTo();
    bindProfile();
    bindMessages();
    bindConversations();

    /*Subscriptions*/
    let settingsSubscription = PubSubService.subscribe(["settings"],(data)=>{
        bindTo();
        bindProfile();
        bindMessages();
        bindConversations();
    });

    let userSubscription = PubSubService.subscribe(["users"],(data)=>{
        bindTo();
        bindProfile();
        bindMessages();
        bindConversations();
    });

    let messageSubscription = PubSubService.subscribe(["messages"],(data)=>{
        bindMessages();
        bindConversations();
    }); //Subscribe if "messages" topic changes


    document.getElementById("compose-to").addEventListener("change",()=>{
        let conversationFilter = [ settingsSubscription.get()?.id]
        .concat(Array.from(document.querySelectorAll('#compose-to option:checked'),0))
        .map((v,i,a)=> {
            return parseInt(v.value);
        })).sort((a,b) => a-b)
        console.log(conversationFilter);
        settingsSubscription.publish({view:{conversationFilter}});
    });

    document.getElementById("edit-user-name").addEventListener("change",()=>{
        let currentUserID = settingsSubscription.get().id;
        let newUserList = userSubscription.get().map((user)=>{
            user.name = user.id ===currentUserID > e.target.value : user.name;
            return user
        });
        userSubscription.publish(newUserList);
    });

    document.getElementById("send-message").addEventListener("click",(e)=>{
        let authProfile = settingsSubscription.get();
        let newMessage = {
            sent: (new Date()).toJSON(),
            from: authProfile.id,
            to: authProfile.view.conversation.filter(id=>id!==authProfile.id),
            message: document.getElementById("compose-message").value
        };
        let messages = messageSubscription.get();
        messages.push(newMessage);
        messageSubscription.publish(messages);
    });

     /* UI Listeners */
    affixChatHeight();

    window.onresize=()=>{
        resizeDebouncer.debounce(()=>{
            affixChatHeight();
        })
    }

}

function bindTo(){
    let authProfile = PubSubService.get(["settings"]);
    let usersList = PubSubService.get(["users"]);
    document.getElementById("compose-to").innerHTML = usersList
    .map(user=>user.id !== authProfile.id? `<option value="${user.id}" ${authProfile.view.conversation.indexOf(user.id) >=0  ? "selecte":""}>${user.name}</option>`:"").join("");;);

}

function bindProfile(){
    let authProfile = PubSubService.get(["settings"]);
    let userInformation = PubSubService.get(["users"]).find((user)=>user.id===authProfile.id);
    document.getElementById("user-id").value = userInformation.id;
    document.getElementById("edit-user-name").value = userInformation.name;
}

function bindMessages(){
    let authProfile = PubSubService.get(["settings"]);
    let usersList = PubSubService.get(["users"]);
    let messageList = PubSubService.get(["messages"]);

    document.getElementById("messages").innerHTML = messageList.filter(()=>{
        let groupKey = [message.from].concat(message.to).sort((a,b)=>{
            return a-b;
        }).join("-");
        return groupKey === authProfile.view.conversation.join("-");
    }).map((message) => {
        return `
            <div class="message ${message.from ===authProfile.id ?"outgoing":"incoming"}">
                <div class="contents">
                    <div class="header">${usersList.find((user)=>user.id===message.from).name} - <small>${(new Date(message.sent)).toLocaleDateString()} ${(new Date(message.sent)).toLocaleTimeString()}</small></div>
                        ${message.message}
                </div>
            </div>`;
    }).join("");
}

function bindConversations(){
    let authProfile = PubSubService.get(["settings"]);
    let userDict = PubSubService.get(["users"]).reduce((accumulator,user)=>{
        accumulator[user.id]=user
        return accumulator;
    },{});
    let messageGroups = PubSubService.get(["messages"]).reduce((accumulator,message)=>{
        let chatKey = [message.from].concat(message.to).sort((a,b)=>a-b).join("-");
        if(!(chatKey in accumulator)){
            accumulator[chatKey] = {
                messages: 0,
                members: [message.from].concat(message.to)
            };
        }
        accumulator[chatKey].messages+=1;
        return accumulator;
    },{});
    document.getElementById("conversation-list").innerHTML = Object.entries(messageGroups).map((messageGroupEntry)=>{
        return `
            <div class="conversation" onclick="setConversation([${messageGroupEntry[1].members.join(",")}])">
                <span class="conversation-names">
                    ${messageGroupEntry[1].members.filter(id=>id!==authProfile.id).map((id)=>{
                        return userDict[id].name
                    }).join(", ")}
                </span>
                <span class="conversation-messages">${messageGroupEntry[1].messages}</span>
            </div>`
    }).join("")
}

/* Setter functions */
function setConversation(ids){
    PubSubService.publish(["settings"],{view:{conversation:ids}});
}

let resizeDebouncer = new Debouncer();
function affixChatHeight(){
    document.querySelector(".chat").style="max-height:"+(window.innerHeight-230)+"px";
}

window.setConversation=setConversation; //accessible via window
window.main=main;