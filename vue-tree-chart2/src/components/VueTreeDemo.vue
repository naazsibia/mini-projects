<template>
  <div class="container">
    <h3>
      Example of multiple parents with node collapse disabled
    </h3>
    <div style="display: flex;">
      <v-btn @click="controlScale('bigger')">+</v-btn>
      <v-btn @click="controlScale('smaller')">-</v-btn>
      <v-btn @click="controlScale('restore')">1:1</v-btn>
    </div>
    <vue-tree
      ref = 'graphTree'
      style="width: 800px; height: 600px; border: 1px solid gray;"
      :dataset="courses"
      :config="treeConfig"
      :collapse-enabled="true"
      linkStyle="straight"
    > <!--linkStyle="straight" would go up there -->
      <template v-slot:node="{ node, collapsed }">
        <div
          class="rich-media-node"
          :style="{ border: collapsed ? '2px solid grey' : '' }"
        >
          <span style="padding: 4px 0; font-weight: bold;"
            >{{ node.name }}</span
          >
        </div>
      </template>
    </vue-tree>
  </div>
</template>

<script>
import VueTree from '../vue-tree/VueTree.vue'

export default {
  name: 'treemap',
  components: { 'vue-tree': VueTree },
  data() {
    return {
      courses: {
        name: 'CS',
        children: [
          {
            name: 'MAT135H5',
            children: [{name: 'STA256H5'}]
          },
          {
            name: 'CSC108H5',
            children: [
              {
                name: 'CSC148H5',
                children: [{name: 'CSC207H5'}, 
                          {name: 'CSC236H5', children: [{name: 'CSC263H5', children: [{name: 'CSC373H5'}]}, {name: 'CSC363H5'}]}
                          ]
              }
            ]
          },
          {
            name: 'MAT102H5'
          },
        ],
        links: [
          {parent: 'MAT102H5', child: 'CSC236H5'},
          {parent: 'STA256H5', child: 'CSC263H5'}
        ],
        identifier: 'name',
      },
      treeConfig: { nodeWidth: 120, nodeHeight: 80, levelHeight: 200 }
    }
  },
  computed: {
    multiRootChoice() {
      if (this.clicked) {
        return this.multiRoot2
      }
      return this.multiRoot1
    }
  },
  methods: {
    controlScale(command) {
      switch (command) {
        case 'bigger':
          this.$refs.graphTree.zoomIn()
          break
        case 'smaller':
          this.$refs.graphTree.zoomOut()
          break
        case 'restore':
          this.$refs.graphTree.restoreScale()
          break
      }
    }
  }
}
</script>

<style scoped lang="less">
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.tree-node {
  display: inline-block;
  width: 28px;
  height: 28px;
  border-radius: 50%;
  background-color: antiquewhite;
  text-align: center;
  line-height: 28px;
}

.rich-media-node {
  width: 80px;
  padding: 8px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: center;
  color: white;
  background-color: #f7c616;
  border-radius: 4px;
}

h3 {
  margin-top: 32px;
  margin-bottom: 16px;
}

.changeDataset {
  font-size: 1rem;
  font-weight: 200;
  letter-spacing: 1px;
  padding: 10px 45px 10px;
  outline: 0;
  border: 1px solid black;
  cursor: pointer;
  margin: 1rem;
  position: relative;
  background-color: rgb(33, 150, 243);
  color: whitesmoke;
}
</style>
