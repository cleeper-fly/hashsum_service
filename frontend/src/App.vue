<template>
   <div class="file">
   <form @submit.prevent="fileSubmit" enctype="multipart/form-data">
      <div class="fields">
        <label>Upload File</label><br/>
        <input
          type="file"
          ref="file"
          v-on:change="onSelect"
        />
      </div>
      <div class="fields">
        <button>Submit</button>
      </div>
      <div class="message">
        <h5>Task id : {{message}}</h5>
        <h5>{{send_context}}</h5>
      </div>
   </form>
   <form @submit.prevent="textSubmit">
      <div class="fields">
        <label>Get result</label><br/>
        <input
          type="text"
          ref="text"
          v-model="text"
        >
      </div>
      <div class="fields">
        <button>Submit</button>
      </div>
      <div class="message">
        <h5>Task id : {{result}}</h5>
        <h5>MD5 sum: {{sum}}</h5>
        <h5>{{get_context}}</h5>
      </div>
   </form>
   </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'FileUpload',
  data() {
    return {
      file:"",
      message:"",
      sum:"",
      result:"",
      text:"",
      send_context:"",
      get_context:""
    }
  },
  methods: {
    onSelect(){
      const file = this.$refs.file.files[0];
      this.file = file;
    },
    fileSubmit(){
      const formData = new FormData();
      formData.append('uploaded_file',this.file);
      axios.post('http://' + location.host + '/api/v1/hash/calculate-file-hash',
        formData
      )
      .then((response) => {
        this.message = response.data.task_id
        console.log(response)
        this.send_context = 'Successfully send!'
      })
      .catch(function (error) {
        console.log(error);
      });
    },
    textSubmit(){
      const text = this.text
      axios.get('http://' + location.host + '/api/v1/hash/get-result/' + text
      )
      .then((response) => {
        this.result = response.data.task_id
        this.sum = response.data.result_hash
        this.get_context = 'Task found!'
        console.log(response)
      })
      .catch(function (error) {
        if (error.response){
          console.log(error.response)
        } else {
          console.log(error)
        }
      });
    }
  },
}
</script>
