{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Gallery for All</title>
    <link rel="stylesheet" href="{% static 'css/styles.css' %}">
    <script src="https://kit.fontawesome.com/727277d0a7.js" crossorigin="anonymous"></script>
</head>
<body>
{% for post in posts %}
    <div class="main-container">
        <h2>News Categories</h2>
        <p> Lorem Ipsum, dolor sit amet consictatur adipicing elit. Aut, velit.</p>
        <div class="filter-container">
            <div class="category-head">
                <ul>
                    <div class="category-title active" id="all">
                        <li>All</li>
                        <span><i class="fas fa-border-all"></i></span>
                    </div>
                    <div class="category-title" id="culture">
                        <li>Culture</li>
                        <span><i class="fas fa-theater-masks"></i></span>
                    </div>
                    <div class="category-title" id="politics">
                        <li>Politics</li>
                        <span><i class="fas fa-landmark"></i></span>
                    </div>
                    <div class="category-title" id="finance">
                        <li>Finance</li>
                        <span><i class="fas fa-chart-area"></i></span>
                    </div>
                    <div class="category-title" id="business">
                        <li>Business</li>
                        <span><i class="fas fa-coins"></i></span>
                    </div>
                    <div class="category-title" id="sports">
                        <li>Sports</li>
                        <span><i class="fas fa-running"></i></span>
                    </div>
                </ul>
            </div>
            <div class="posts-collect">
                <div class="posts-main-container">
                    <!-- single post -->

                    <div class="all business">
                        <div class="post-img">
                            <img src="{% static 'images/image1.jpg' %}" alt="post">
                            <span class="category-name">Business</span>
                        </div>
                        <div class="post-content">
                            <div class="post-content-top">
                                <span><i class="fas fa-calendar"></i>January 01, 2xxx</span>
                                <span><i class="fas fa-comment"></i>34</span>
                            </div>
                            <h2>Lorem ipsum dolor sit amet</h2><p>Lorem ipsum dolor sit amet consectetur adipisicing elit.</p>
                        </div>
                        <button type="button" class="read-btn">Read All</button>
                    </div>

                    <!-- end of single post -->

                    <!-- single post -->

                    <div class="all culture">
                        <div class="post-img">
                            <img src="{% static 'images/image1.jpg' %}" alt="post">
                            <span class="category-name">Culture</span>
                        </div>
                        <div class="post-content">
                            <div class="post-content-top">
                                <span><i class="fas fa-calendar"></i>January 01, 2xxx</span>
                                <span><i class="fas fa-comment"></i>34</span>
                            </div>
                        <h2>Lorem ipsum dolor sit amet</h2><p>Lorem ipsum dolor sit amet consectetur adipisicing elit.</p>
                        </div>
                        <button type="button" class="read-btn">Read All</button>
                    </div>

                    <!-- end of single post -->

                    <!-- single post -->

                    <div class="all politics">
                        <div class="post-img">
                            <img src="{% static 'images/image1.jpg' %}" alt="post">
                            <span class="category-name">Politics</span>
                        </div>
                        <div class="post-content">
                            <div class="post-content-top">
                                <span><i class="fas fa-calendar"></i>January 01, 2xxx</span>
                                <span><i class="fas fa-comment"></i>34</span>
                            </div>
                            <h2>Lorem ipsum dolor sit amet</h2><p>Lorem ipsum dolor sit amet consectetur adipisicing elit.</p>
                        </div>
                        <button type="button" class="read-btn">Read All</button>
                    </div>

                    <!-- end of single post -->

                    <!-- single post -->

                    <div class="all finance">
                        <div class="post-img">
                            <img src="{% static 'images/image1.jpg' %}" alt="post">
                            <span class="category-name">Finance</span>
                        </div>
                        <div class="post-content">
                            <div class="post-content-top">
                                <span><i class="fas fa-calendar"></i>January 01, 2xxx</span>
                                <span><i class="fas fa-comment"></i>34</span>
                            </div>
                            <h2>Lorem ipsum dolor sit amet</h2><p>Lorem ipsum dolor sit amet consectetur adipisicing elit.</p>
                        </div>
                        <button type="button" class="read-btn">Read All</button>
                    </div>

                    <!-- end of single post -->

                    <!-- single post -->

                    <div class="all sports">
                        <div class="post-img">
                            <img src="{% static 'images/image1.jpg' %}" alt="post">
                            <span class="category-name">Sports</span>
                        </div>
                        <div class="post-content">
                            <div class="post-content-top">
                                <span><i class="fas fa-calendar"></i>January 01, 2xxx</span>
                                <span><i class="fas fa-comment"></i>34</span>
                            </div>
                            <h2>Lorem ipsum dolor sit amet</h2><p>Lorem ipsum dolor sit amet consectetur adipisicing elit.</p>
                        </div>
                        <button type="button" class="read-btn">Read All</button>
                    </div>

                    <!-- end of single post -->
                </div>
            </div>
        </div>
    </div>
{% endfor %}
</body>
<script type="text/javascript" src="{% static 'js/main.js' %}" defer> </script>
</html>