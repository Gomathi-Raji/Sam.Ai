# Particle UI Features - Perplexity AI Style

## Overview
Enhanced the orb UI with a dynamic particle system that expands and collapses based on speech rate, pitch, and volume in both listening and speaking modes.

## Key Features

### 1. **Dynamic Particle Expansion/Collapse**
- Particles orbit around the center in an elliptical pattern
- Orbit radius expands and collapses based on audio analysis
- Smooth transitions between states

### 2. **Audio-Reactive Animations**

#### **Listening Mode (Green)**
- 🎤 Analyzes microphone input in real-time
- Particles expand based on voice volume
- Orbital patterns respond to speech rate
- Connection strength varies with pitch
- **Expansion Factor**: 0.8 - 2.3x based on audio input

#### **Speaking Mode (Orange/Red)**
- 🔊 Simulates audio response during AI speech
- Continuous pulsing animation synchronized with speech
- Dynamic particle size changes with simulated pitch
- Enhanced glow effects during speech
- **Expansion Factor**: 1.0 - 3.0x based on speech synthesis

#### **Processing Mode (Purple)**
- ⚙️ Smooth breathing/pulsing animation
- Gentle wave motion
- Indicates AI is thinking
- **Expansion Factor**: 1.0 - 1.3x with sine wave pulse

#### **Ready Mode (Blue)**
- 💤 Idle breathing animation
- Subtle expansion/contraction
- Low-energy particle movement
- **Expansion Factor**: 0.95 - 1.05x gentle pulse

### 3. **Visual Effects**

#### **Particle Properties**
- Orbital motion around center point
- Size: 2-3px (scales with audio)
- Opacity: 0.3-0.8 (varies with expansion)
- Glow effect during high audio activity
- Wave motion based on speech rate

#### **Connections**
- Dynamic connection distance (150-200px base)
- Line thickness responds to volume (1-3px)
- Opacity scales with audio intensity
- Limited to 5 connections per particle (performance)

#### **Central Glow**
- Radial gradient from center
- Size: 150-450px (scales with expansion)
- Intensity: 0.2-0.5 (based on audio)
- Color matches current state

### 4. **Audio Analysis**

#### **Volume Detection**
- Range: 0-1 (normalized)
- Affects: particle size, connection opacity, central glow
- Update rate: Real-time (60 FPS)

#### **Pitch Detection**
- Range: 0-1 (normalized frequency)
- Affects: particle radius variation, expansion factor
- Based on dominant frequency in FFT analysis

#### **Rate Detection**
- Range: 0-1 (spectral energy distribution)
- Affects: wave motion, orbital speed
- Calculated from high/low frequency ratio

### 5. **State Configurations**

| State | Color | Particles | Connections | Speed | Expansion |
|-------|-------|-----------|-------------|-------|-----------|
| Ready | Blue | 150 | 150px | 0.3x | 1.0x |
| Listening | Green | 200 | 180px | 0.8x | 1.5x |
| Speaking | Orange | 250 | 200px | 1.2x | 2.0x |
| Processing | Purple | 180 | 160px | 0.6x | 1.2x |

### 6. **Performance Optimizations**
- Canvas fade effect for motion blur
- Limited connection drawing (max 5 per particle)
- Efficient FFT analysis (2048 bins)
- Smooth interpolation for expansion changes
- RequestAnimationFrame for 60 FPS rendering

### 7. **Interactive Features**
- Mouse repulsion (particles avoid cursor within 150px)
- Touch support for mobile devices
- Click to manually trigger listening
- Responsive canvas (auto-resize)

## Technical Implementation

### **Audio Context**
- Web Audio API for microphone analysis
- FFT size: 2048 for detailed frequency analysis
- Real-time frequency and time domain analysis

### **Speech Synthesis Monitoring**
- Boundary events for word-level tracking
- Simulated audio metrics during synthesis
- Smooth fade-in/fade-out transitions
- Error handling and cleanup

### **Animation System**
- 60 FPS rendering loop
- Smooth state transitions (10% interpolation)
- Phase offsets for natural particle variation
- Sine/cosine wave combinations for organic motion

## Browser Compatibility
- ✅ Chrome/Edge (recommended)
- ✅ Firefox
- ✅ Safari (limited speech synthesis features)
- ✅ Mobile browsers (touch support)

## Usage
1. Open web UI at `http://localhost:8080`
2. Click "Tap to Start Zara" to enable audio
3. Speak when particles turn green (listening)
4. Watch particles expand and pulse during your speech
5. Observe different animation patterns during AI response

## Future Enhancements
- [ ] Direct speech synthesis audio capture (when browser APIs improve)
- [ ] Advanced frequency visualization (spectrum bars)
- [ ] Color transitions based on emotion/sentiment
- [ ] 3D particle effects with WebGL
- [ ] Custom particle shapes (stars, dots, triangles)
