<template>
	<div class="Container">
	 
	  <div class="image-container">
		<img src="../assets/TP.jpg" alt="Static Image">

	  </div>
	</div>
  </template>
  <style lang="scss" scoped>
  .Container {
	padding: 0 12px 12px 12px;
	border-radius: 5px;
	height: calc(100vh - 69px);
  }
  
  .image-container {
  
	width: 100%;
	height: 100%;
	display: flex;
	justify-content: center;
	align-items: center;
  
	img {
	  max-width: 100%;
	  max-height: 100%;
	}
  }
  </style>