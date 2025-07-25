let topics = {
    settings:{
        id:1,
        view:{
            conversation:[1,2,3]
        }
    },
    users:[
        { id:1, name: "Ryan" },
        { id:2, name: "Sarah" },
        { id:3, name: "Emma" }
    ],
    messages:[
        {   sent:"2021-06-02T11:50:00",
            from:1, to:[2], message:"I'd like to learn a bit more about pub sub models" },
        {   sent:"2021-06-02T11:52:00",
            from:2, to:[1], message:"No problem, start a conversation with Emma and I and we can discuss it's benefits" },
        {   sent:"2021-06-02T12:10:00",
            from:1, to:[2,3], message:"Hey, can anyone tell me what benefits a pubsub model has?" },
        {   sent:"2021-06-02T12:12:00",
            from:2, to:[1,3], message:"It allows one-way binding from a single publishing component to the central repository for other components to see" },
        {   sent:"2021-06-02T12:13:00",
            from:3, to:[1,2], message:"It also simplifies and removes the need for cross component communication" }
    ]
}