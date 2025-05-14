import * as THREE from 'https://cdn.skypack.dev/three';

let scene, camera, renderer, card;
let lifted = false, revealed = false;

init();
animate();

function init() {
  scene = new THREE.Scene();
  camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 1, 1000);
  camera.position.z = 5;

  renderer = new THREE.WebGLRenderer({ antialias: true });
  renderer.setSize(window.innerWidth, window.innerHeight);
  document.body.appendChild(renderer.domElement);

  // 카드 1장
  const geometry = new THREE.PlaneGeometry(2, 3);
  const material = new THREE.MeshBasicMaterial({ color: 0x222222 });
  card = new THREE.Mesh(geometry, material);
  scene.add(card);
}

function animate() {
  requestAnimationFrame(animate);

  if (!lifted) {
    card.position.y += 0.02;
    if (card.position.y >= 1.5) lifted = true;
  } else if (!revealed) {
    card.rotation.y += 0.05;
    if (card.rotation.y >= Math.PI) {
      card.material.color.set(0xffcc00);
      revealResult();
      revealed = true;
    }
  }

  renderer.render(scene, camera);
}

function revealResult() {
  const result = document.getElementById("result");
  result.style.opacity = 1;
}