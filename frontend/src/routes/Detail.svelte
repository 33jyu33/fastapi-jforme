<script>
    import fastapi from "../lib/api"
    import Error from "../components/Error.svelte"
    import { push } from 'svelte-spa-router'

    export let params = {}
    let question_id = params.question_id
    let question = {answers:[]}
    let content = ""
    let error = {detail:[]}

    function get_question(){
        fastapi("get", "/api/question/detail/"+question_id, {}, (json) => {
            question = json
        })
    }
    get_question()

    function post_answer(event){
        event.preventDefault()
        let url = "/api/answer/create/" + question_id
        let params = {
            content:content
        }
        fastapi('post', url, params,
            (json) => {
                content = ''
                error = {detail:[]}
                get_question()
            },
            (err_json) => {
                error = err_json
            }
        )
    }
</script>

<h1>{question.subject}</h1>
<div>
    {question.content}
</div>
<div>
    {question.create_date}
</div>
<button on:click = "{() => {
    push('/')
}}">목록으로</button>"
<h5 class="border-bottom my-3 py-2">{question.answers.length}개의 답변이 있습니다.</h5>
<ul>
    {#each question.answers as answer}
        <li>{answer.content}</li>
    {/each}
</ul>
<Error error={error}/>
<form method="post">
    <textarea rows = "15" bind:value={content}></textarea>
    <input type="submit" value="create answer" on:click="{post_answer}">
</form>
<style>
    textarea {
        width:100%;
    }
    input[type=submit] {
        margin-top:10px;
    }    
</style>