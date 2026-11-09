# Milestone-3

# Personal Design Decisions
When designing my code for Milestone 3, I was met with different questions about how I would handle certain cases
The questions were as follows:
1. What happens when og_tag and alt_tag are given, but name_xformer is given too?
2. What happens when only og_tag or alt_tag are given, but not both?
3. What happens if no arguments are given to a SoupReplacer object?

Based on these questions, I made these decisions:
1. A ValueError is thrown. Only one form of tag name replacement can exist. By implementing the SoupReplacer this way, there is no confusion as to how a given tag's name is changed.
2. A ValueError is thrown. Both str arguments (og_tag and alt_tag) must be given if the user decides to use it in the way that Milestone 2 implements it.
3. Nothing happens, as all of the xformer functions are None.

Additionally, to keep track of the changes and properly close tags, I added a str variable called og_name to the Tag class.
Upon the initialization of a Tag instance, tag.og_name is set to the name argument given, and never changes.
In __init__.py, popTag(), pushTag(), and _popToTag() look at tag.og_name instead of the potentially modified tag.name
While this may add another layer of complexity for those who may build upon my modifications, I found it to cost less space compared to an additional stack that would track the various modifications through the xformer functions.

# Comparing SoupReplacer (Milestone 2 vs 3)
__Milestone 2__
My Milestone 2 SoupReplacer was simple and clear in terms of its capabilities. It made aspects of the existing API more efficient due to it making modifications during parsing (like Milestone 3 still does). Additionally, it was minimally invasive, as it only changed the BeautifulSoup initializers by adding the SoupReplacer argument and a few lines to the handle_starttag and handle_endtag methods. If a user only needed to change the Tag object names in a document, this would be a good implementation to use.

__Milestone 3__
My Milestone 3 SoupReplacer was more complex and powerful than that of Milestone 2. It gives the user much more capabilities in modifying a document upon parsing, and flexibility how they would go about modifying the document. The challenges with this is that there is less control in knowing how my SoupReplacer would be used. As mentioned earlier, the Tag class gained the og_name variable that stores the name given upon a Tag object's initialization. In allowing a variety of Tag modifications, there are more dependencies involved if someone were to expand upon the code I have written.

__My Recommendation:__
Despite the costs involved with the Milestone 3 implementation, I would recommend this version of my SoupReplacer. This implementation allows for the user to be able to do so much more than Milestone 2. Especially with SoupReplacer modifying Tag objects at parse time, it improves the efficiency of the API and decreases the amount of API calls that a user makes in their application code. If my "team" were to build another extension to this API, I would suggest this implementation for the reasons I described as long as it does not greatly increase the amount of dependencies overall (i.e. severely changing the implementation of a Tag object, etc.). 