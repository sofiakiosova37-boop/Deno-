import * as THREE from 'three';
import * as dat from 'dat.gui';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 5000);
camera.position.set(-175, 115, 5);
scene.background = new THREE.Color(0x000000);

const renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.toneMapping = THREE.ACESFilmicToneMapping;
document.body.appendChild(renderer.domElement);

const controls = new OrbitControls(camera, renderer.domElement);
controls.enableDamping = true;
controls.dampingFactor = 0.05;
controls.screenSpacePanning = false;

const textureLoader = new THREE.TextureLoader();

const settings = {
    acceleration: 1,      
    accelerationOrbit: 1  
};

// ******  Сонце  ******
const sunSize = 697/40; 
const sunGeom = new THREE.SphereGeometry(sunSize, 32, 20);
const sunTexture = textureLoader.load('/static/image/sun.jpg');
const sunMat = new THREE.MeshStandardMaterial({
    map: sunTexture,
    emissive: 0xffcc00,
    emissiveMap: sunTexture,
    emissiveIntensity: 1.5
});
const sun = new THREE.Mesh(sunGeom, sunMat);
scene.add(sun);
//
const sunLight = new THREE.PointLight(0xffffff, 2, 500); 
sunLight.position.set(0, 0, 0);
scene.add(sunLight); // сонце світиться
const ambientLight = new THREE.AmbientLight(0x404040, 1.5); 
scene.add(ambientLight); // загальне світло

// ****** Функція для планет ******
const planetObjects = [];
function createPlanet(planetName, size, position, tilt, texturePath, ring) {
    const planetTexture = textureLoader.load(texturePath);
    planetTexture.anisotropy = renderer.capabilities.getMaxAnisotropy();
    const mesh = new THREE.Mesh(
        new THREE.SphereGeometry(size, 64, 64),
        new THREE.MeshStandardMaterial({ 
            map: planetTexture,
            metalness: 0.1,
            roughness: 0.8
        })
    );
    mesh.userData = { name: planetName }; 
    const planetSystem = new THREE.Group();
    const orbitGroup = new THREE.Object3D();
    mesh.position.x = position;
    mesh.rotation.z = tilt * Math.PI / 180;
    planetSystem.add(mesh);
    // orbit
    const orbitPath = new THREE.EllipseCurve( 0, 0, position, position);
    const orbitGeometry = new THREE.BufferGeometry().setFromPoints(orbitPath.getPoints(100));
    const orbitLine = new THREE.LineLoop(orbitGeometry, new THREE.LineBasicMaterial({ color: 0xffffff, opacity: 0.1, transparent: true }));
    orbitLine.rotation.x = Math.PI / 2;
    scene.add(orbitLine);
// Кільця
if(ring)
  {
    const ringTexture = textureLoader.load(ring.texturePath);
    const ringGeom = new THREE.RingGeometry(ring.innerRadius, ring.outerRadius, 64);
    const ringMesh = new THREE.Mesh(
            new THREE.RingGeometry(ring.innerRadius, ring.outerRadius, 64),
            new THREE.MeshStandardMaterial({ 
                map: ringTexture,
                side: THREE.DoubleSide, 
                transparent: true, 
                opacity: 0.8, 
                alphaTest: 0.05
            })
        );
        const pos = ringMesh.geometry.attributes.position;
        const uv = ringGeom.attributes.uv;
        const v3 = new THREE.Vector3();
        for (let i = 0; i < pos.count; i++) {
        v3.fromBufferAttribute(pos, i);
        const distance = v3.length();
        const u = (distance - ring.innerRadius) / (ring.outerRadius - ring.innerRadius);
        uv.setXY(i, u, 1); 
    }
    uv.needsUpdate = true;
        const ringMat = new THREE.MeshStandardMaterial({ 
            map: ringTexture,
            side: THREE.DoubleSide, 
            transparent: true, 
            opacity: 0.9, 
            alphaTest: 0.05
        });
    ringMesh.position.x = position;
    ringMesh.rotation.x = -0.5 * Math.PI;
    ringMesh.rotation.y = -tilt * Math.PI / 180;
    planetSystem.add(ringMesh);
  }
  orbitGroup.add(planetSystem);
  scene.add(orbitGroup);
  const timeScale = 0.02;
  const orbitSpeed = (1 / Math.sqrt(position)) * timeScale;
  planetObjects.push({ orbitGroup, mesh, orbitSpeed });
}
// ****** Створення планет ******
createPlanet('Mercury', 2.4, 40, 0, '/static/image/mercury.jpg');
createPlanet('Venus', 6.1, 65, 177, '/static/image/venusmap.jpg');
createPlanet('Earth', 6.4, 90, 23.5, '/static/image/earth_daymap.jpg');
createPlanet('Mars', 3.4, 115, 25, '/static/image/marsmap.jpg');
createPlanet('Jupiter', 69/4, 200, 3, '/static/image/jupiter.jpg');
createPlanet('Saturn', 58/4, 270, 26, '/static/image/saturnmap.jpg', {
    innerRadius: 18, 
    outerRadius: 29,
    texturePath: '/static/image/saturn_ring.png'
});
createPlanet('Uranus', 25/4, 320, 97, '/static/image/uranus.jpg', {
    innerRadius: 10, 
    outerRadius: 12,
    texturePath: '/static/image/uranus_ring.png'
});
createPlanet('Neptune', 24/4, 350, 28, '/static/image/neptune.jpg');
createPlanet('Pluto', 1.2, 380, 122, '/static/image/plutomap.jpg');

// Інтерактив у формі кліків 
const raycaster = new THREE.Raycaster();
const mouse = new THREE.Vector2();
let selectedPlanet = null;
let isMovingTowardsPlanet = false;
let targetCameraPosition = new THREE.Vector3();
function onMouseDown(event) {
    mouse.x = (event.clientX / window.innerWidth) * 2 - 1;
    mouse.y = -(event.clientY / window.innerHeight) * 2 + 1;
    raycaster.setFromCamera(mouse, camera);
    const intersects = raycaster.intersectObjects(planetObjects.map(p => p.mesh));
    if (intersects.length > 0) {
        const clicked = intersects[0].object;
        selectedPlanet = planetObjects.find(p => p.mesh === clicked);
        if (selectedPlanet) {
            settings.accelerationOrbit = 0; 
            const planetPos = new THREE.Vector3();
            clicked.getWorldPosition(planetPos);
            targetCameraPosition.copy(planetPos).add(new THREE.Vector3(0, 20, 50));
            isMovingTowardsPlanet = true;
            showPlanetInfo(clicked.userData.name);
        }
    }
 }
function showPlanetInfo(name) {
    const infoDiv = document.getElementById('planetInfo');
    const data = planetsData[name];
        if (data) {
            document.getElementById('planetName').innerText = name;
            document.getElementById('planetDetails').innerHTML = `
                <div style="margin-bottom: 10px; font-style: italic;">${data.info}</div>
                <hr>
                <b>Радіус:</b> ${data.radius}<br>
                <b>Відстань до Сонця:</b> ${data.distance}<br>
                <b>Період оберту (рік):</b> ${data.orbit}<br>
                <b>Тривалість дня:</b> ${data.rotation}<br>
                <b>Нахил осі:</b> ${data.tilt}<br>
                <b>Супутники:</b> ${data.moons}
            `; 
            infoDiv.style.display = 'block';
        }
    }

window.showPlanetInfo = function(name) {
    const infoDiv = document.getElementById('planetInfo');
    const data = planetsData[name];
    if (data && infoDiv) {
        document.getElementById('planetName').innerText = name;
        document.getElementById('planetDetails').innerHTML = `
            <div style="margin-bottom: 10px; font-style: italic;">${data.info}</div>
            <hr>
            <b>Радіус:</b> ${data.radius}<br>
            <b>Відстань:</b> ${data.distance}<br>
            <b>Період оберту:</b> ${data.orbit}<br>
            <b>Супутники:</b> ${data.moons}
        `; 
        infoDiv.style.display = 'block'; 
    }
};
window.closeInfo = function() {
    const infoDiv = document.getElementById('planetInfo');
    if(infoDiv) infoDiv.style.display = 'none';
    settings.accelerationOrbit = 1; 
    isMovingTowardsPlanet = false;
}
// Анімація
function animate() {
    requestAnimationFrame(animate);
    if (!isMovingTowardsPlanet) {
        planetObjects.forEach(obj => {
            obj.orbitGroup.rotation.y += obj.orbitSpeed * settings.accelerationOrbit;
            obj.mesh.rotation.y += 0.01 * settings.acceleration;
        });
        sun.rotation.y += 0.005 * settings.acceleration;
    } else {
        camera.position.lerp(targetCameraPosition, 0.05);
        const planetPos = new THREE.Vector3();
        selectedPlanet.mesh.getWorldPosition(planetPos);
        controls.target.lerp(planetPos, 0.05); 
        if (camera.position.distanceTo(targetCameraPosition) < 1) isMovingTowardsPlanet = false;
    }
    controls.update();
    renderer.render(scene, camera);
}
window.addEventListener('mousedown', onMouseDown);
animate();
window.addEventListener('resize', () => {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
});

// Інформація про планети, що з'являється, при їх натисканні
const planetsData = {
    'Mercury': {
        radius: '2,439.7 km',
        tilt: '0.034°',
        rotation: '58.6 Earth days',
        orbit: '88 Earth days',
        distance: '57.9 million km',
        moons: '0',
        info: 'The smallest planet in our solar system and nearest to the Sun.'
    },
    'Venus': {
        radius: '6,051.8 km',
        tilt: '177.4°',
        rotation: '243 Earth days',
        orbit: '225 Earth days',
        distance: '108.2 million km',
        moons: '0',
        info: 'Second planet from the Sun, known for its extreme temperatures and thick atmosphere.'
    },
    'Earth': {
        radius: '6,371 km',
        tilt: '23.5°',
        rotation: '24 hours',
        orbit: '365 days',
        distance: '150 million km',
        moons: '1 (Moon)',
        info: 'Third planet from the Sun and the only known planet to harbor life.'
    },
    'Mars': {
        radius: '3,389.5 km',
        tilt: '25.19°',
        rotation: '1.03 Earth days',
        orbit: '687 Earth days',
        distance: '227.9 million km',
        moons: '2 (Phobos and Deimos)',
        info: 'Known as the Red Planet, famous for its reddish appearance and potential for human colonization.'
    },
    'Jupiter': {
        radius: '69,911 km',
        tilt: '3.13°',
        rotation: '9.9 hours',
        orbit: '12 Earth years',
        distance: '778.5 million km',
        moons: '95 known moons (Ganymede, Callisto, Europa, Io are the 4 largest)',
        info: 'The largest planet in our solar system, known for its Great Red Spot.'
    },
    'Saturn': {
        radius: '58,232 km',
        tilt: '26.73°',
        rotation: '10.7 hours',
        orbit: '29.5 Earth years',
        distance: '1.4 billion km',
        moons: '146 known moons',
        info: 'Distinguished by its extensive ring system, the second-largest planet in our solar system.'
    },
    'Uranus': {
        radius: '25,362 km',
        tilt: '97.77°',
        rotation: '17.2 hours',
        orbit: '84 Earth years',
        distance: '2.9 billion km',
        moons: '27 known moons',
        info: 'Known for its unique sideways rotation and pale blue color.'
    },
    'Neptune': {
        radius: '24,622 km',
        tilt: '28.32°',
        rotation: '16.1 hours',
        orbit: '165 Earth years',
        distance: '4.5 billion km',
        moons: '14 known moons',
        info: 'The most distant planet from the Sun in our solar system, known for its deep blue color.'
    },
    'Pluto': {
        radius: '1,188.3 km',
        tilt: '122.53°',
        rotation: '6.4 Earth days',
        orbit: '248 Earth years',
        distance: '5.9 billion km',
        moons: '5 (Charon, Styx, Nix, Kerberos, Hydra)',
        info: 'Originally classified as the ninth planet, Pluto is now considered a dwarf planet.'
    }
};