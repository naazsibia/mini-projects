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
        name: 'CS',
        _children: [{'name': 'CSC108H5', 'id': 'CSC108H5', '_children': [{'name': 'CSC148H5', 'id': 'CSC148H5', '_children': [{'name': 'CSC207H5', 'id': 'CSC207H5', '_children': [{'name': 'CSC209H5', 'id': 'CSC209H5', '_children': [{'name': 'CSC301H5', 'id': 'CSC301H5', '_children': [{'name': 'or', 'id': 'OR_CSC301H5/CSC318H5/CSC384H5', '_children': [{'name': 'CSC404H5', 'id': 'CSC404H5'}]}]}, {'name': 'CSC309H5', 'id': 'CSC309H5', '_children': [{'name': 'and', 'id': 'and_CSC309H5-CSC369H5-CSC373H5', '_children': [{'name': 'CSC409H5', 'id': 'CSC409H5'}]}]}, {'name': 'CSC333H5', 'id': 'CSC333H5', '_children': [{'name': 'and', 'id': 'and_CSC333H5-CSC369H5', '__children': [{'name': 'CSC423H5', 'id': 'CSC423H5'}]}]}, {'name': 'and', 'id': 'and_CSC209H5-CSC236H5', '_children': [{'name': 'CSC347H5', 'id': 'CSC347H5', '_children': [{'name': 'and', 'id': 'and_CSC347H5-CSC369H5', '_children': [{'name': 'CSC427H5', 'id': 'CSC427H5'}]}]}]}, {'name': 'and', 'id': 'and_CSC209H5-CSC258H5-CSC263H5', '_children': [{'name': 'CSC358H5', 'id': 'CSC358H5'}, {'name': 'CSC458H5', 'id': 'CSC458H5'}]}, {'name': 'and', 'id': 'and_CSC209H5-CSC258H5', '_children': [{'name': 'CSC367H5', 'id': 'CSC367H5'}, {'name': 'CSC369H5', 'id': 'CSC369H5', '_children': [{'name': 'and', 'id': 'and_CSC309H5-CSC369H5-CSC373H5', '_children': [{'name': 'CSC409H5', 'id': 'CSC409H5'}]}, {'name': 'and', 'id': 'and_CSC333H5-CSC369H5', '_children': [{'name': 'CSC423H5', 'id': 'CSC423H5'}]}, {'name': 'and', 'id': 'and_CSC347H5-CSC369H5', '_children': [{'name': 'CSC427H5', 'id': 'CSC427H5'}]}, {'name': 'CSC469H5', 'id': 'CSC469H5'}]}]}, {'name': 'and', 'id': 'and_CSC209H5-CSC376H5-OR_MAT223H5/MAT240H5-STA256H5', '_children': [{'name': 'CSC375H5', 'id': 'CSC375H5'}]}, {'name': 'and', 'id': 'and_CSC209H5-CSC258H5-OR_MAT223H5/MAT240H5', '_children': [{'name': 'CSC376H5', 'id': 'CSC376H5', '_children': [{'name': 'and', 'id': 'and_CSC209H5-CSC376H5-OR_MAT223H5/MAT240H5-STA256H5', '_children': [{'name': 'CSC375H5', 'id': 'CSC375H5'}]}, {'name': 'and', 'id': 'and_CSC338H5-CSC376H5-MAT224H5', '_children': [{'name': 'CSC476H5', 'id': 'CSC476H5'}]}, {'name': 'and', 'id': 'and_CSC209H5-CSC376H5-MAT232H5-OR_MAT223H5/MAT240H5-STA256H5', '_children': [{'name': 'CSC477H5', 'id': 'CSC477H5'}]}]}]}, {'name': 'and', 'id': 'and_CSC209H5-CSC376H5-MAT232H5-OR_MAT223H5/MAT240H5-STA256H5', '_children': [{'name': 'CSC477H5', 'id': 'CSC477H5'}]}]}, {'name': 'and', 'id': 'and_CSC207H5-CSC236H5-OR_STA107H5/STA256H5', '_children': [{'name': 'CSC263H5', 'id': 'CSC263H5', '_children': [{'name': 'and', 'id': 'and_CSC148H5-CSC263H5-OR_MAT134H5/MAT136H5/MAT134Y5/MAT135Y5/MAT137Y5/MAT157Y5/MAT233H5-OR_MAT223H5/MAT240H5', '_children': [{'name': 'CSC338H5', 'id': 'CSC338H5', '_children': [{'name': 'and', 'id': 'and_CSC263H5-CSC338H5', '_children': [{'name': 'CSC420H5', 'id': 'CSC420H5'}]}, {'name': 'and', 'id': 'and_CSC338H5-CSC376H5-MAT224H5', '_children': [{'name': 'CSC476H5', 'id': 'CSC476H5'}]}]}]}, {'name': 'CSC343H5', 'id': 'CSC343H5'}, {'name': 'CSC373H5', 'id': 'CSC373H5', '_children': [{'name': 'and', 'id': 'and_CSC309H5-CSC369H5-CSC373H5', '_children': [{'name': 'CSC409H5', 'id': 'CSC409H5'}]}]}, {'name': 'and', 'id': 'and_CSC209H5-CSC258H5-CSC263H5', '_children': [{'name': 'CSC358H5', 'id': 'CSC358H5'}, {'name': 'CSC458H5', 'id': 'CSC458H5'}]}, {'name': 'and', 'id': 'and_CSC263H5-CSC338H5', '_children': [{'name': 'CSC420H5', 'id': 'CSC420H5'}]}, {'name': 'and', 'id': 'and_CSC258H5-CSC263H5-CSC324H5', '_children': [{'name': 'CSC488H5', 'id': 'CSC488H5'}]}]}]}, {'name': 'and', 'id': 'and_CSC207H5-MAT232H5-OR_MAT223H5/MAT240H5-STA256H5', '_children': [{'name': 'CSC311H5', 'id': 'CSC311H5', '_children': [{'name': 'and', 'id': 'and_CSC311H5-STA256H5', '_children': [{'name': 'CSC475H5', 'id': 'CSC475H5'}]}, {'name': 'or', 'id': 'OR_CSC311H5/CSC411H5', '_children': [{'name': 'CSC413H5', 'id': 'CSC413H5'}]}]}]}, {'name': 'and', 'id': 'and_CSC207H5-MAT223H5', '_children': [{'name': 'CSC320H5', 'id': 'CSC320H5'}]}, {'name': 'and', 'id': 'and_CSC207H5-CSC236H5', '_children': [{'name': 'CSC324H5', 'id': 'CSC324H5', '_children': [{'name': 'and', 'id': 'and_CSC324H5-STA256H5', '_children': [{'name': 'CSC384H5', 'id': 'CSC384H5', '_children': [{'name': 'or', 'id': 'OR_CSC301H5/CSC318H5/CSC384H5', '_children': [{'name': 'CSC404H5', 'id': 'CSC404H5'}]}]}]}, {'name': 'and', 'id': 'and_CSC258H5-CSC263H5-CSC324H5', '_children': [{'name': 'CSC488H5', 'id': 'CSC488H5'}]}]}]}, {'name': 'and', 'id': 'and_CSC207H5-CSC318H5-STA256H5', '_children': [{'name': 'CSC428H5', 'id': 'CSC428H5'}]}]}, {'name': 'CSC290H5', 'id': 'CSC290H5'}, {'name': 'and', 'id': 'and_CSC148H5-MAT102H5', '_children': [{'name': 'CSC236H5', 'id': 'CSC236H5', '_children': [{'name': 'and', 'id': 'and_CSC207H5-CSC236H5-OR_STA107H5/STA256H5', '_children': [{'name': 'CSC263H5', 'id': 'CSC263H5', '_children': [{'name': 'and', 'id': 'and_CSC148H5-CSC263H5-OR_MAT134H5/MAT136H5/MAT134Y5/MAT135Y5/MAT137Y5/MAT157Y5/MAT233H5-OR_MAT223H5/MAT240H5', '_children': [{'name': 'CSC338H5', 'id': 'CSC338H5', '_children': [{'name': 'and', 'id': 'and_CSC263H5-CSC338H5', '_children': [{'name': 'CSC420H5', 'id': 'CSC420H5'}]}, {'name': 'and', 'id': 'and_CSC338H5-CSC376H5-MAT224H5', '_children': [{'name': 'CSC476H5', 'id': 'CSC476H5'}]}]}]}, {'name': 'CSC343H5', 'id': 'CSC343H5'}, {'name': 'CSC373H5', 'id': 'CSC373H5', '_children': [{'name': 'and', 'id': 'and_CSC309H5-CSC369H5-CSC373H5', '_children': [{'name': 'CSC409H5', 'id': 'CSC409H5'}]}]}, {'name': 'and', 'id': 'and_CSC209H5-CSC258H5-CSC263H5', '_children': [{'name': 'CSC358H5', 'id': 'CSC358H5'}, {'name': 'CSC458H5', 'id': 'CSC458H5'}]}, {'name': 'and', 'id': 'and_CSC263H5-CSC338H5', '_children': [{'name': 'CSC420H5', 'id': 'CSC420H5'}]}, {'name': 'and', 'id': 'and_CSC258H5-CSC263H5-CSC324H5', '_children': [{'name': 'CSC488H5', 'id': 'CSC488H5'}]}]}]}, {'name': 'and', 'id': 'and_CSC207H5-CSC236H5', '_children': [{'name': 'CSC324H5', 'id': 'CSC324H5', '_children': [{'name': 'and', 'id': 'and_CSC324H5-STA256H5', '_children': [{'name': 'CSC384H5', 'id': 'CSC384H5', '_children': [{'name': 'or', 'id': 'OR_CSC301H5/CSC318H5/CSC384H5', '_children': [{'name': 'CSC404H5', 'id': 'CSC404H5'}]}]}]}, {'name': 'and', 'id': 'and_CSC258H5-CSC263H5-CSC324H5', '_children': [{'name': 'CSC488H5', 'id': 'CSC488H5'}]}]}]}, {'name': 'and', 'id': 'and_CSC209H5-CSC236H5', '_children': [{'name': 'CSC347H5', 'id': 'CSC347H5', '_children': [{'name': 'and', 'id': 'and_CSC347H5-CSC369H5', '_children': [{'name': 'CSC427H5', 'id': 'CSC427H5'}]}]}]}, {'name': 'and', 'id': 'and_CSC236H5-CSC363H5', '_children': [{'name': 'CSC448H5', 'id': 'CSC448H5'}]}, {'name': 'or', 'id': 'OR_CSC236H5/CSC238H5/MAT202H5', '_children': [{'name': 'CSC363H5', 'id': 'CSC363H5', '_children': [{'name': 'CSC422H5', 'id': 'CSC422H5'}, {'name': 'and', 'id': 'and_CSC236H5-CSC363H5', '_children': [{'name': 'CSC448H5', 'id': 'CSC448H5'}]}]}]}]}, {'name': 'CSC258H5', 'id': 'CSC258H5', '_children': [{'name': 'and', 'id': 'and_CSC209H5-CSC258H5-CSC263H5', '_children': [{'name': 'CSC358H5', 'id': 'CSC358H5'}, {'name': 'CSC458H5', 'id': 'CSC458H5'}]}, {'name': 'and', 'id': 'and_CSC209H5-CSC258H5', '_children': [{'name': 'CSC367H5', 'id': 'CSC367H5'}, {'name': 'CSC369H5', 'id': 'CSC369H5', '_children': [{'name': 'and', 'id': 'and_CSC309H5-CSC369H5-CSC373H5', '_children': [{'name': 'CSC409H5', 'id': 'CSC409H5'}]}, {'name': 'and', 'id': 'and_CSC333H5-CSC369H5', '_children': [{'name': 'CSC423H5', 'id': 'CSC423H5'}]}, {'name': 'and', 'id': 'and_CSC347H5-CSC369H5', '_children': [{'name': 'CSC427H5', 'id': 'CSC427H5'}]}, {'name': 'CSC469H5', 'id': 'CSC469H5'}]}]}, {'name': 'and', 'id': 'and_CSC209H5-CSC258H5-OR_MAT223H5/MAT240H5', '_children': [{'name': 'CSC376H5', 'id': 'CSC376H5', '_children': [{'name': 'and', 'id': 'and_CSC209H5-CSC376H5-OR_MAT223H5/MAT240H5-STA256H5', '_children': [{'name': 'CSC375H5', 'id': 'CSC375H5'}]}, {'name': 'and', 'id': 'and_CSC338H5-CSC376H5-MAT224H5', '_children': [{'name': 'CSC476H5', 'id': 'CSC476H5'}]}, {'name': 'and', 'id': 'and_CSC209H5-CSC376H5-MAT232H5-OR_MAT223H5/MAT240H5-STA256H5', '_children': [{'name': 'CSC477H5', 'id': 'CSC477H5'}]}]}]}, {'name': 'and', 'id': 'and_CSC258H5-CSC263H5-CSC324H5', '_children': [{'name': 'CSC488H5', 'id': 'CSC488H5'}]}]}]}, {'name': 'and', 'id': 'and_CSC148H5-MAT223H5-STA256H5', '_children': [{'name': 'CSC310H5', 'id': 'CSC310H5'}]}, {'name': 'and', 'id': 'and_CSC148H5-CSC263H5-OR_MAT134H5/MAT136H5/MAT134Y5/MAT135Y5/MAT137Y5/MAT157Y5/MAT233H5-OR_MAT223H5/MAT240H5', '_children': [{'name': 'CSC338H5', 'id': 'CSC338H5', '_children': [{'name': 'and', 'id': 'and_CSC263H5-CSC338H5', '_children': [{'name': 'CSC420H5', 'id': 'CSC420H5'}]}, {'name': 'and', 'id': 'and_CSC338H5-CSC376H5-MAT224H5', '_children': [{'name': 'CSC476H5', 'id': 'CSC476H5'}]}]}]}]}]}],
        links: [{parent: 'CSC108H5', child: 'CSC148H5'}, {parent: 'CSC148H5', child: 'CSC207H5'}, {parent: 'CSC148H5', child: 'CSC290H5'}, {parent: 'CSC148H5', child: 'and_CSC148H5-MAT102H5'}, {parent: 'CSC148H5', child: 'and_CSC148H5-MAT223H5-STA256H5'}, {parent: 'CSC148H5', child: 'and_CSC148H5-CSC263H5-OR_MAT134H5/MAT136H5/MAT134Y5/MAT135Y5/MAT137Y5/MAT157Y5/MAT233H5-OR_MAT223H5/MAT240H5'}, {parent: 'CSC207H5', child: 'CSC209H5'}, {parent: 'CSC207H5', child: 'and_CSC207H5-CSC236H5-OR_STA107H5/STA256H5'}, {parent: 'CSC207H5', child: 'and_CSC207H5-MAT232H5-OR_MAT223H5/MAT240H5-STA256H5'}, {parent: 'CSC207H5', child: 'and_CSC207H5-MAT223H5'}, {parent: 'CSC207H5', child: 'and_CSC207H5-CSC236H5'}, {parent: 'CSC207H5', child: 'and_CSC207H5-CSC318H5-STA256H5'}, {parent: 'MAT102H5', child: 'and_CSC148H5-MAT102H5'}, {parent: 'and_CSC148H5-MAT102H5', child: 'CSC236H5'}, {parent: 'and_CSC148H5-MAT102H5', child: 'CSC258H5'}, {parent: 'CSC236H5', child: 'and_CSC207H5-CSC236H5-OR_STA107H5/STA256H5'}, {parent: 'CSC236H5', child: 'and_CSC207H5-CSC236H5'}, {parent: 'CSC236H5', child: 'and_CSC209H5-CSC236H5'}, {parent: 'CSC236H5', child: 'and_CSC236H5-CSC363H5'}, {parent: 'CSC236H5', child: 'OR_CSC236H5/CSC238H5/MAT202H5'}, {parent: 'OR_STA107H5/STA256H5', child: 'and_CSC207H5-CSC236H5-OR_STA107H5/STA256H5'}, {parent: 'and_CSC207H5-CSC236H5-OR_STA107H5/STA256H5', child: 'CSC263H5'}, {parent: 'CSC209H5', child: 'CSC301H5'}, {parent: 'CSC209H5', child: 'CSC309H5'}, {parent: 'CSC209H5', child: 'CSC333H5'}, {parent: 'CSC209H5', child: 'and_CSC209H5-CSC236H5'}, {parent: 'CSC209H5', child: 'and_CSC209H5-CSC258H5-CSC263H5'}, {parent: 'CSC209H5', child: 'and_CSC209H5-CSC258H5'}, {parent: 'CSC209H5', child: 'and_CSC209H5-CSC376H5-OR_MAT223H5/MAT240H5-STA256H5'}, {parent: 'CSC209H5', child: 'and_CSC209H5-CSC258H5-OR_MAT223H5/MAT240H5'}, {parent: 'CSC209H5', child: 'and_CSC209H5-CSC376H5-MAT232H5-OR_MAT223H5/MAT240H5-STA256H5'}, {parent: 'MAT223H5', child: 'and_CSC148H5-MAT223H5-STA256H5'}, {parent: 'MAT223H5', child: 'and_CSC207H5-MAT223H5'}, {parent: 'MAT223H5', child: 'OR_MAT223H5/MAT240H5'}, {parent: 'STA256H5', child: 'and_CSC148H5-MAT223H5-STA256H5'}, {parent: 'STA256H5', child: 'and_CSC207H5-MAT232H5-OR_MAT223H5/MAT240H5-STA256H5'}, {parent: 'STA256H5', child: 'and_CSC209H5-CSC376H5-OR_MAT223H5/MAT240H5-STA256H5'}, {parent: 'STA256H5', child: 'and_CSC324H5-STA256H5'}, {parent: 'STA256H5', child: 'and_CSC207H5-CSC318H5-STA256H5'}, {parent: 'STA256H5', child: 'and_CSC311H5-STA256H5'}, {parent: 'STA256H5', child: 'and_CSC209H5-CSC376H5-MAT232H5-OR_MAT223H5/MAT240H5-STA256H5'}, {parent: 'STA256H5', child: 'OR_STA107H5/STA256H5'}, {parent: 'and_CSC148H5-MAT223H5-STA256H5', child: 'CSC310H5'}, {parent: 'MAT232H5', child: 'and_CSC207H5-MAT232H5-OR_MAT223H5/MAT240H5-STA256H5'}, {parent: 'MAT232H5', child: 'and_CSC209H5-CSC376H5-MAT232H5-OR_MAT223H5/MAT240H5-STA256H5'}, {parent: 'OR_MAT223H5/MAT240H5', child: 'and_CSC207H5-MAT232H5-OR_MAT223H5/MAT240H5-STA256H5'}, {parent: 'OR_MAT223H5/MAT240H5', child: 'and_CSC148H5-CSC263H5-OR_MAT134H5/MAT136H5/MAT134Y5/MAT135Y5/MAT137Y5/MAT157Y5/MAT233H5-OR_MAT223H5/MAT240H5'}, {parent: 'OR_MAT223H5/MAT240H5', child: 'and_CSC209H5-CSC376H5-OR_MAT223H5/MAT240H5-STA256H5'}, {parent: 'OR_MAT223H5/MAT240H5', child: 'and_CSC209H5-CSC258H5-OR_MAT223H5/MAT240H5'}, {parent: 'OR_MAT223H5/MAT240H5', child: 'and_CSC209H5-CSC376H5-MAT232H5-OR_MAT223H5/MAT240H5-STA256H5'}, {parent: 'and_CSC207H5-MAT232H5-OR_MAT223H5/MAT240H5-STA256H5', child: 'CSC311H5'}, {parent: 'and_CSC207H5-MAT223H5', child: 'CSC320H5'}, {parent: 'MAT301H5', child: 'and_MAT301H5-OR_MAT224H5/MAT240H5'}, {parent: 'OR_MAT224H5/MAT240H5', child: 'and_MAT301H5-OR_MAT224H5/MAT240H5'}, {parent: 'and_MAT301H5-OR_MAT224H5/MAT240H5', child: 'CSC322H5'}, {parent: 'and_CSC207H5-CSC236H5', child: 'CSC324H5'}, {parent: 'CSC263H5', child: 'and_CSC148H5-CSC263H5-OR_MAT134H5/MAT136H5/MAT134Y5/MAT135Y5/MAT137Y5/MAT157Y5/MAT233H5-OR_MAT223H5/MAT240H5'}, {parent: 'CSC263H5', child: 'CSC343H5'}, {parent: 'CSC263H5', child: 'CSC373H5'}, {parent: 'CSC263H5', child: 'and_CSC209H5-CSC258H5-CSC263H5'}, {parent: 'CSC263H5', child: 'and_CSC263H5-CSC338H5'}, {parent: 'CSC263H5', child: 'and_CSC258H5-CSC263H5-CSC324H5'}, {parent: 'OR_MAT134H5/MAT136H5/MAT134Y5/MAT135Y5/MAT137Y5/MAT157Y5/MAT233H5', child: 'and_CSC148H5-CSC263H5-OR_MAT134H5/MAT136H5/MAT134Y5/MAT135Y5/MAT137Y5/MAT157Y5/MAT233H5-OR_MAT223H5/MAT240H5'}, {parent: 'and_CSC148H5-CSC263H5-OR_MAT134H5/MAT136H5/MAT134Y5/MAT135Y5/MAT137Y5/MAT157Y5/MAT233H5-OR_MAT223H5/MAT240H5', child: 'CSC338H5'}, {parent: 'and_CSC209H5-CSC236H5', child: 'CSC347H5'}, {parent: 'CSC258H5', child: 'and_CSC209H5-CSC258H5-CSC263H5'}, {parent: 'CSC258H5', child: 'and_CSC209H5-CSC258H5'}, {parent: 'CSC258H5', child: 'and_CSC209H5-CSC258H5-OR_MAT223H5/MAT240H5'}, {parent: 'CSC258H5', child: 'and_CSC258H5-CSC263H5-CSC324H5'}, {parent: 'and_CSC209H5-CSC258H5-CSC263H5', child: 'CSC358H5'}, {parent: 'and_CSC209H5-CSC258H5-CSC263H5', child: 'CSC458H5'}, {parent: 'OR_CSC236H5/CSC238H5/MAT202H5', child: 'CSC363H5'}, {parent: 'and_CSC209H5-CSC258H5', child: 'CSC367H5'}, {parent: 'and_CSC209H5-CSC258H5', child: 'CSC369H5'}, {parent: 'CSC376H5', child: 'and_CSC209H5-CSC376H5-OR_MAT223H5/MAT240H5-STA256H5'}, {parent: 'CSC376H5', child: 'and_CSC338H5-CSC376H5-MAT224H5'}, {parent: 'CSC376H5', child: 'and_CSC209H5-CSC376H5-MAT232H5-OR_MAT223H5/MAT240H5-STA256H5'}, {parent: 'and_CSC209H5-CSC376H5-OR_MAT223H5/MAT240H5-STA256H5', child: 'CSC375H5'}, {parent: 'and_CSC209H5-CSC258H5-OR_MAT223H5/MAT240H5', child: 'CSC376H5'}, {parent: 'CSC324H5', child: 'and_CSC324H5-STA256H5'}, {parent: 'CSC324H5', child: 'and_CSC258H5-CSC263H5-CSC324H5'}, {parent: 'and_CSC324H5-STA256H5', child: 'CSC384H5'}, {parent: 'OR_CSC301H5/CSC318H5/CSC384H5', child: 'CSC404H5'}, {parent: 'CSC309H5', child: 'and_CSC309H5-CSC369H5-CSC373H5'}, {parent: 'CSC369H5', child: 'and_CSC309H5-CSC369H5-CSC373H5'}, {parent: 'CSC369H5', child: 'and_CSC333H5-CSC369H5'}, {parent: 'CSC369H5', child: 'and_CSC347H5-CSC369H5'}, {parent: 'CSC369H5', child: 'CSC469H5'}, {parent: 'CSC373H5', child: 'and_CSC309H5-CSC369H5-CSC373H5'}, {parent: 'and_CSC309H5-CSC369H5-CSC373H5', child: 'CSC409H5'}, {parent: 'OR_CSC311H5/CSC411H5', child: 'CSC413H5'}, {parent: 'CSC338H5', child: 'and_CSC263H5-CSC338H5'}, {parent: 'CSC338H5', child: 'and_CSC338H5-CSC376H5-MAT224H5'}, {parent: 'and_CSC263H5-CSC338H5', child: 'CSC420H5'}, {parent: 'CSC363H5', child: 'CSC422H5'}, {parent: 'CSC363H5', child: 'and_CSC236H5-CSC363H5'}, {parent: 'CSC333H5', child: 'and_CSC333H5-CSC369H5'}, {parent: 'and_CSC333H5-CSC369H5', child: 'CSC423H5'}, {parent: 'CSC347H5', child: 'and_CSC347H5-CSC369H5'}, {parent: 'and_CSC347H5-CSC369H5', child: 'CSC427H5'}, {parent: 'CSC318H5', child: 'and_CSC207H5-CSC318H5-STA256H5'}, {parent: 'CSC318H5', child: 'OR_CSC301H5/CSC318H5/CSC384H5'}, {parent: 'and_CSC207H5-CSC318H5-STA256H5', child: 'CSC428H5'}, {parent: 'and_CSC236H5-CSC363H5', child: 'CSC448H5'}, {parent: 'CSC311H5', child: 'and_CSC311H5-STA256H5'}, {parent: 'CSC311H5', child: 'OR_CSC311H5/CSC411H5'}, {parent: 'and_CSC311H5-STA256H5', child: 'CSC475H5'}, {parent: 'MAT224H5', child: 'and_CSC338H5-CSC376H5-MAT224H5'}, {parent: 'MAT224H5', child: 'OR_MAT224H5/MAT240H5'}, {parent: 'and_CSC338H5-CSC376H5-MAT224H5', child: 'CSC476H5'}, {parent: 'and_CSC209H5-CSC376H5-MAT232H5-OR_MAT223H5/MAT240H5-STA256H5', child: 'CSC477H5'}, {parent: 'and_CSC258H5-CSC263H5-CSC324H5', child: 'CSC488H5'}, {parent: 'STA107H5', child: 'OR_STA107H5/STA256H5'}, {parent: 'MAT240H5', child: 'OR_MAT223H5/MAT240H5'}, {parent: 'MAT240H5', child: 'OR_MAT224H5/MAT240H5'}, {parent: 'MAT134H5', child: 'OR_MAT134H5/MAT136H5/MAT134Y5/MAT135Y5/MAT137Y5/MAT157Y5/MAT233H5'}, {parent: 'MAT136H5', child: 'OR_MAT134H5/MAT136H5/MAT134Y5/MAT135Y5/MAT137Y5/MAT157Y5/MAT233H5'}, {parent: 'MAT134Y5', child: 'OR_MAT134H5/MAT136H5/MAT134Y5/MAT135Y5/MAT137Y5/MAT157Y5/MAT233H5'}, {parent: 'MAT135Y5', child: 'OR_MAT134H5/MAT136H5/MAT134Y5/MAT135Y5/MAT137Y5/MAT157Y5/MAT233H5'}, {parent: 'MAT137Y5', child: 'OR_MAT134H5/MAT136H5/MAT134Y5/MAT135Y5/MAT137Y5/MAT157Y5/MAT233H5'}, {parent: 'MAT157Y5', child: 'OR_MAT134H5/MAT136H5/MAT134Y5/MAT135Y5/MAT137Y5/MAT157Y5/MAT233H5'}, {parent: 'MAT233H5', child: 'OR_MAT134H5/MAT136H5/MAT134Y5/MAT135Y5/MAT137Y5/MAT157Y5/MAT233H5'}, {parent: 'CSC238H5', child: 'OR_CSC236H5/CSC238H5/MAT202H5'}, {parent: 'MAT202H5', child: 'OR_CSC236H5/CSC238H5/MAT202H5'}, {parent: 'CSC301H5', child: 'OR_CSC301H5/CSC318H5/CSC384H5'}, {parent: 'CSC384H5', child: 'OR_CSC301H5/CSC318H5/CSC384H5'}, {parent: 'CSC411H5', child: 'OR_CSC311H5/CSC411H5'}],
        identifier: 'id',
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
